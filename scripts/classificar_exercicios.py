"""
Classifica os enunciados do cb-dataset com o Claude (API da Anthropic), em lotes.

Pré-requisitos:
    pip install anthropic
    export ANTHROPIC_API_KEY="sk-ant-..."        (Windows PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-...")
    Ter rodado antes: python scripts/indexar_exercicios.py   (gera classificacao/enunciados_unicos.jsonl e indice_exercicios.csv)

Uso (de qualquer pasta):
    python scripts/classificar_exercicios.py                 # classifica tudo
    python scripts/classificar_exercicios.py --limite 40     # teste rápido com 40 enunciados
    python scripts/classificar_exercicios.py --lote 20 --modelo claude-sonnet-5-5

O script é retomável: se parar no meio, rode de novo e ele pula os ids já classificados.

Saídas (pasta classificacao/):
    classificacao.csv          -> uma linha por enunciado único (id;categoria;subtema;...)
    exercicios_classificados.csv -> índice completo (uma linha por exercício) + classificação
    resumo_por_categoria.csv   -> nº de enunciados, exercícios e códigos de alunos por categoria/subtema
    para_revisar.csv           -> itens com confiança média/baixa ou rótulos fora da taxonomia
    execucao.json              -> modelo, data, tamanho do lote e prompt usados (para a metodologia)
"""
import argparse
import csv
import json
import os
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone

import anthropic # type: ignore

TAXONOMIA = {
    "fundamentos": ["entrada_saida", "condicionais", "lacos", "funcoes", "vetores_matrizes",
                    "strings_basico", "structs", "ponteiros"],
    "recursao": ["recursao_simples", "recursao_multipla", "backtracking"],
    "estruturas_lineares": ["lista_encadeada", "lista_duplamente_encadeada", "pilha", "fila", "deque"],
    "ordenacao": ["bubble_sort", "selection_sort", "insertion_sort", "merge_sort", "quick_sort",
                  "heap_sort", "shell_sort", "counting_sort", "radix_sort", "bucket_sort",
                  "ordenacao_generica"],
    "busca": ["busca_sequencial", "busca_binaria"],
    "hash": ["tabela_hash"],
    "strings_avancado": ["processamento_cadeias", "casamento_padroes"],
    "arvores": ["arvore_binaria", "abb", "avl", "outras_balanceadas", "heap_estrutura"],
    "grafos": ["representacao", "bfs", "dfs", "ordenacao_topologica", "menor_caminho", "arvore_geradora"],
    "complexidade": ["analise_complexidade"],
    "outro": ["outro"],
}

PROMPT = """Você é um especialista em ensino de Algoritmos e Estruturas de Dados. Sua tarefa é classificar exercícios de programação de uma plataforma de juiz online usada nas disciplinas AED I (ICC002) e AED II (ICC003) da UFAM.

## Entrada
Cada linha abaixo é um objeto JSON com os campos: id, titulo, disciplina, linguagem, ocorrencias, total_alunos, enunciado.

## Taxonomia (use EXATAMENTE estes rótulos)
Categorias e subtemas permitidos:

- fundamentos: entrada_saida | condicionais | lacos | funcoes | vetores_matrizes | strings_basico | structs | ponteiros
- recursao: recursao_simples | recursao_multipla | backtracking
- estruturas_lineares: lista_encadeada | lista_duplamente_encadeada | pilha | fila | deque
- ordenacao: bubble_sort | selection_sort | insertion_sort | merge_sort | quick_sort | heap_sort | shell_sort | counting_sort | radix_sort | bucket_sort | ordenacao_generica
- busca: busca_sequencial | busca_binaria
- hash: tabela_hash
- strings_avancado: processamento_cadeias | casamento_padroes
- arvores: arvore_binaria | abb | avl | outras_balanceadas | heap_estrutura
- grafos: representacao | bfs | dfs | ordenacao_topologica | menor_caminho | arvore_geradora
- complexidade: analise_complexidade
- outro: outro

## Regras
1. Classifique pelo que o aluno PRECISA IMPLEMENTAR para resolver o exercício, não apenas pelo título ou pelo contexto da história do enunciado.
2. "categoria" = o conteúdo central avaliado. Se um exercício envolve um tópico avançado (ex.: inserção em ABB) usando outro como meio (ex.: recursão), a categoria é o tópico avançado.
3. "categoria_secundaria" = outro conteúdo relevante exigido, se houver; caso contrário, deixe vazio.
4. Exercícios que usam uma função pronta da linguagem (ex.: sort() do Python, qsort() do C) sem exigir implementar o algoritmo NÃO são "ordenacao": classifique pelo tema principal e mencione isso na justificativa.
5. Se o enunciado pedir para contar trocas, comparações ou passos de um algoritmo específico, classifique no algoritmo correspondente.
6. Use "ordenacao_generica" apenas quando o exercício exige implementar uma ordenação sem especificar qual.
7. "confianca":
   - alta = o enunciado deixa o tema explícito;
   - media = o tema é inferido, mas com boa evidência;
   - baixa = enunciado ambíguo, incompleto ou fora da taxonomia.
8. Não invente informação. Se o enunciado estiver vazio ou truncado, use confianca=baixa e explique.
9. Classifique TODAS as linhas recebidas, na mesma ordem, sem pular nenhuma.

## Saída
Responda SOMENTE com CSV, separador ponto e vírgula, com cabeçalho, sem texto antes ou depois e sem bloco de código:

id;categoria;subtema;categoria_secundaria;confianca;justificativa

- "justificativa": no máximo 20 palavras, em português, sem ponto e vírgula.

## Exercícios
"""

CAMPOS = ["id", "categoria", "subtema", "categoria_secundaria", "confianca", "justificativa"]
RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PASTA = os.path.join(RAIZ_PROJETO, "classificacao")
ARQ_CLASS = os.path.join(PASTA, "classificacao.csv")
ARQ_INDICE = os.path.join(PASTA, "indice_exercicios.csv")


def carregar_enunciados(caminho):
    with open(caminho, encoding="utf-8") as f:
        return [json.loads(l) for l in f if l.strip()]


def carregar_ja_classificados():
    if not os.path.exists(ARQ_CLASS):
        return {}
    with open(ARQ_CLASS, encoding="utf-8") as f:
        return {r["id"]: r for r in csv.DictReader(f, delimiter=";")}


def salvar_linhas(linhas):
    novo = not os.path.exists(ARQ_CLASS)
    with open(ARQ_CLASS, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS, delimiter=";")
        if novo:
            w.writeheader()
        w.writerows(linhas)


def interpretar_csv(texto, ids_esperados):
    """Converte a resposta do modelo em dicts; ignora cabeçalho, cercas de código e linhas estranhas."""
    resultado = {}
    for linha in texto.strip().splitlines():
        linha = linha.strip()
        if not linha or linha.startswith("```") or linha.lower().startswith("id;"):
            continue
        partes = [p.strip() for p in linha.split(";", 5)]
        if len(partes) < 6 or partes[0] not in ids_esperados:
            continue
        resultado[partes[0]] = dict(zip(CAMPOS, partes))
    return resultado


def classificar_lote(cliente, modelo, lote, tentativas=3):
    entrada = "\n".join(json.dumps(e, ensure_ascii=False) for e in lote)
    ids = {e["id"] for e in lote}
    for t in range(tentativas):
        try:
            resp = cliente.messages.create(
                model=modelo,
                max_tokens=8000,
                messages=[{"role": "user", "content": PROMPT + entrada}],
            )
            texto = "".join(b.text for b in resp.content if b.type == "text")
            return interpretar_csv(texto, ids)
        except (anthropic.RateLimitError, anthropic.APIStatusError, anthropic.APIConnectionError) as e:
            espera = 20 * (t + 1)
            print(f"   erro da API ({e.__class__.__name__}); nova tentativa em {espera}s", file=sys.stderr)
            time.sleep(espera)
    return {}


def gerar_relatorios(enunciados):
    classif = carregar_ja_classificados()

    # 1) Itens para revisão manual
    revisar = []
    for r in classif.values():
        problemas = []
        if r["categoria"] not in TAXONOMIA:
            problemas.append("categoria fora da taxonomia")
        elif r["subtema"] not in TAXONOMIA[r["categoria"]]:
            problemas.append("subtema não pertence à categoria")
        if r["categoria_secundaria"] and r["categoria_secundaria"] not in TAXONOMIA:
            problemas.append("categoria secundária fora da taxonomia")
        if r["confianca"] != "alta":
            problemas.append(f"confiança {r['confianca']}")
        if problemas:
            revisar.append({**r, "motivo_revisao": ", ".join(problemas)})
    with open(os.path.join(PASTA, "para_revisar.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=CAMPOS + ["motivo_revisao"], delimiter=";")
        w.writeheader()
        w.writerows(revisar)

    # 2) Índice completo (uma linha por exercício) com a classificação
    total_por_cat = defaultdict(lambda: {"enunciados": set(), "exercicios": 0, "codigos": 0})
    if os.path.exists(ARQ_INDICE):
        with open(ARQ_INDICE, encoding="utf-8") as f:
            indice = list(csv.DictReader(f))
        campos_saida = [c for c in indice[0].keys() if c != "enunciado"] + CAMPOS[1:]
        with open(os.path.join(PASTA, "exercicios_classificados.csv"), "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=campos_saida, delimiter=";", extrasaction="ignore")
            w.writeheader()
            for ex in indice:
                c = classif.get(ex["hash_enunciado"], {})
                linha = {**ex, **{k: c.get(k, "") for k in CAMPOS[1:]}}
                w.writerow(linha)
                chave = (c.get("categoria", "nao_classificado"), c.get("subtema", ""))
                total_por_cat[chave]["enunciados"].add(ex["hash_enunciado"])
                total_por_cat[chave]["exercicios"] += 1
                total_por_cat[chave]["codigos"] += int(ex["n_alunos"])

    # 3) Resumo por categoria/subtema (o que importa para o sorteio de 200 códigos)
    with open(os.path.join(PASTA, "resumo_por_categoria.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["categoria", "subtema", "enunciados_unicos", "exercicios", "codigos_alunos"])
        for (cat, sub), v in sorted(total_por_cat.items()):
            w.writerow([cat, sub, len(v["enunciados"]), v["exercicios"], v["codigos"]])

    print(f"\n{len(classif)}/{len(enunciados)} enunciados classificados; {len(revisar)} marcados para revisão.")
    print("\nCódigos de alunos por categoria:")
    por_cat = defaultdict(int)
    for (cat, _), v in total_por_cat.items():
        por_cat[cat] += v["codigos"]
    for cat, n in sorted(por_cat.items(), key=lambda x: -x[1]):
        aviso = "  <-- menos de 200" if n < 200 else ""
        print(f"  {cat:22s} {n:6d}{aviso}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=os.path.join(PASTA, "enunciados_unicos.jsonl"))
    ap.add_argument("--modelo", default="claude-opus-5-5")
    ap.add_argument("--lote", type=int, default=20, help="enunciados por chamada (padrão 20)")
    ap.add_argument("--limite", type=int, default=0, help="classificar só os N primeiros (teste)")
    ap.add_argument("--so-relatorio", action="store_true", help="não chama a API, só refaz os relatórios")
    args = ap.parse_args()

    os.makedirs(PASTA, exist_ok=True)
    enunciados = carregar_enunciados(args.entrada)
    if args.limite:
        enunciados = enunciados[: args.limite]

    if not args.so_relatorio:
        ja = carregar_ja_classificados()
        pendentes = [e for e in enunciados if e["id"] not in ja]
        print(f"{len(enunciados)} enunciados, {len(ja)} já classificados, {len(pendentes)} pendentes.")

        cliente = anthropic.Anthropic()
        lotes = [pendentes[i:i + args.lote] for i in range(0, len(pendentes), args.lote)]
        for n, lote in enumerate(lotes, 1):
            print(f"Lote {n}/{len(lotes)} ({len(lote)} itens)...")
            res = classificar_lote(cliente, args.modelo, lote)
            faltando = [e for e in lote if e["id"] not in res]
            if faltando:  # reenvia uma vez só os ids que vieram faltando
                print(f"   {len(faltando)} ids sem resposta; reenviando.")
                res.update(classificar_lote(cliente, args.modelo, faltando))
            salvar_linhas([res[e["id"]] for e in lote if e["id"] in res])
            ainda = [e["id"] for e in lote if e["id"] not in res]
            if ainda:
                print(f"   AVISO: não classificados neste lote: {', '.join(ainda)} (rode de novo depois)")

        with open(os.path.join(PASTA, "execucao.json"), "w", encoding="utf-8") as f:
            json.dump({
                "data_utc": datetime.now(timezone.utc).isoformat(),
                "modelo": args.modelo,
                "tamanho_lote": args.lote,
                "arquivo_entrada": args.entrada,
                "prompt": PROMPT,
            }, f, ensure_ascii=False, indent=2)

    gerar_relatorios(enunciados)


if __name__ == "__main__":
    main()