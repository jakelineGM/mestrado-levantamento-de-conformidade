"""
Verifica a conformidade enunciado x código dos itens sorteados usando o Claude Code
(CLI `claude -p`), ou seja, pela sua assinatura do Claude, sem chave de API.

Cada chamada recebe UM enunciado e UM código (um item da amostra) e não tem memória
das outras chamadas.

Pré-requisitos:
  - Claude Code instalado e logado com sua conta (rode `claude` uma vez no terminal).
  - A variável ANTHROPIC_API_KEY NÃO pode estar definida, senão o Claude Code cobra na API.
  - Em levantamento-de-conformidade: selecao/amostra.jsonl e o arquivo do prompt (prompt/).

VERSÕES DO PROMPT
  Cada versão do prompt tem sua própria pasta de resultados: conformidade/<versao>/.
  Para testar uma mudança no prompt, salve-o com outro nome e use outra --versao:
      python scripts/verificar_conformidade.py --prompt prompt/prompt_conformidade_V3.txt --versao v3 --limite 20
  O script se recusa a misturar, na mesma versão, resultados de prompts ou modelos diferentes.

Uso:
  python verificar_conformidade.py --limite 20                    # calibração (v2, 20 primeiros)
  python verificar_conformidade.py --uids AED-001,AED1-014        # itens específicos
  python verificar_conformidade.py                                # todos (retoma de onde parou)
  python verificar_conformidade.py --so-relatorio                 # só refaz as planilhas

Saídas (conformidade/<versao>/):
  resultados.jsonl  -> um JSON por item, como a LLM respondeu (+ metadados)
  erros.jsonl       -> itens sem resposta válida (rode de novo para tentar só esses)
  itens.csv         -> uma linha por item, ordenada por prioridade de revisão manual
                       (as colunas revisao_manual_* são suas e são preservadas ao refazer)
  desvios.csv       -> uma linha por desvio apontado (tipo, linhas, evidência)
  execucao.json     -> modelo, datas e prompt exato usado (para a metodologia)

Para o tamanho do problema (proporção de desvios), comparação entre versões e concordância
com a sua revisão manual, use relatorio_conformidade.py.
"""
import argparse
import csv
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone

RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAIZ = os.path.join(RAIZ_PROJETO, "conformidade")
SISTEMA = ("Você é um avaliador acadêmico de código. Siga exatamente as instruções da mensagem "
           "e responda somente com o objeto JSON pedido.")
trava = threading.Lock()

# Tipos de desvio agrupados pela natureza do problema (usado só nos relatórios).
GRUPO_DO_TIPO = {
    "saida_fixa": "saida_fabricada",
    "saida_simulada": "saida_fabricada",
    "funcao_pronta": "metodo_diferente",
    "algoritmo_diferente": "metodo_diferente",
    "estrutura_diferente": "metodo_diferente",
    "requisito_ignorado": "metodo_diferente",
    "outro": "metodo_diferente",
}
VEREDITOS = {"sem_desvio", "desvio", "indeterminado"}
COLUNAS_MANUAIS = ["revisao_manual_desvio", "revisao_manual_comentario"]


# ---------- utilidades ----------
def pasta_da_versao(versao):
    return os.path.join(RAIZ, versao)


def ler_csv_tolerante(caminho):
    """Lê CSV ';' salvo pelo Excel (utf-8 ou ANSI) ou por este script (utf-8 com BOM)."""
    for codificacao in ("utf-8-sig", "cp1252"):
        try:
            with open(caminho, encoding=codificacao, newline="") as f:
                return list(csv.DictReader(f, delimiter=";"))
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Não consegui ler {caminho}")


def carregar_resultados(pasta):
    """Último resultado de cada uid em <pasta>/resultados.jsonl."""
    arq = os.path.join(pasta, "resultados.jsonl")
    regs = {}
    if os.path.exists(arq):
        for linha in open(arq, encoding="utf-8"):
            if linha.strip():
                r = json.loads(linha)
                regs[r["uid"]] = r
    return regs


def tipos_do_registro(r):
    return sorted({d.get("tipo", "") for d in r.get("desvios", []) if d.get("tipo")})


def grupo_do_registro(r):
    grupos = {GRUPO_DO_TIPO.get(t, "metodo_diferente") for t in tipos_do_registro(r)}
    if not grupos:
        return ""
    return grupos.pop() if len(grupos) == 1 else "misto"


# ---------- montagem do prompt ----------
def numerar(codigo):
    return "\n".join(f"{i:4d} | {linha}" for i, linha in enumerate(codigo.splitlines(), 1))


def formatar_casos(casos, n=3, limite=300):
    if not casos:
        return "(sem casos de teste)"
    partes = []
    for i, c in enumerate(casos[:n], 1):
        ent = c["entrada"] if len(c["entrada"]) <= limite else c["entrada"][:limite] + "\n[...cortado]"
        sai = c["saida"] if len(c["saida"]) <= limite else c["saida"][:limite] + "\n[...cortado]"
        partes.append(f"Caso {i}\nEntrada:\n{ent.rstrip()}\nSaída esperada:\n{sai.rstrip()}")
    return "\n\n".join(partes)


def montar_prompt(modelo_prompt, item):
    valores = {
        "{uid}": item["uid"],
        "{linguagem}": item["linguagem"],
        "{titulo}": item["titulo"],
        "{enunciado}": item["enunciado"],
        "{dicas}": item.get("dicas") or "(sem dicas)",
        "{casos_teste}": formatar_casos(item.get("casos_teste", [])),
        "{codigo_numerado}": numerar(item["codigo"]),
    }
    texto = modelo_prompt
    for k, v in valores.items():  # replace simples: o prompt contém chaves de JSON
        texto = texto.replace(k, v)
    return texto


# ---------- chamada ao Claude Code ----------
def extrair_json(texto):
    ini, fim = texto.find("{"), texto.rfind("}")
    if ini < 0 or fim < 0:
        raise ValueError("resposta sem JSON")
    return json.loads(texto[ini:fim + 1])


def chamar_claude(exe, modelo, prompt, pasta_vazia, timeout=600):
    cmd = [exe, "-p", "--model", modelo, "--output-format", "json",
           "--tools", "", "--system-prompt", SISTEMA]
    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True, encoding="utf-8",
                          cwd=pasta_vazia, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError((proc.stderr or proc.stdout).strip()[:500])
    try:
        envelope = json.loads(proc.stdout)
    except json.JSONDecodeError:
        return proc.stdout, None
    if envelope.get("is_error"):
        raise RuntimeError(str(envelope.get("result"))[:500])
    return envelope.get("result", ""), envelope


def validar(r):
    if r.get("veredito") not in VEREDITOS:
        raise ValueError(f"veredito inválido: {r.get('veredito')!r}")
    if r.get("confianca") not in {"alta", "media", "baixa"}:
        raise ValueError(f"confianca inválida: {r.get('confianca')!r}")
    if not isinstance(r.get("exigencias"), list) or not isinstance(r.get("desvios"), list):
        raise ValueError("exigencias/desvios ausentes")
    n = len(r["desvios"])
    if r["veredito"] == "desvio" and n == 0:
        raise ValueError("veredito 'desvio' sem nenhum desvio listado")
    if r["veredito"] != "desvio" and n > 0:
        raise ValueError(f"veredito '{r['veredito']}' mas há {n} desvio(s) listado(s)")
    for d in r["desvios"]:
        if d.get("tipo") not in GRUPO_DO_TIPO:
            raise ValueError(f"tipo de desvio inválido: {d.get('tipo')!r}")
        if not str(d.get("evidencia", "")).strip():
            raise ValueError("desvio sem evidência")


def processar(item, exe, modelo, modelo_prompt, prompt_sha, pasta_vazia, tentativas=2):
    prompt = montar_prompt(modelo_prompt, item)
    ultimo_erro = ""
    for t in range(tentativas):
        try:
            texto, envelope = chamar_claude(exe, modelo, prompt, pasta_vazia)
            r = extrair_json(texto)
            validar(r)
            r["uid"] = item["uid"]
            meta = {k: item[k] for k in ("disciplina", "categoria", "subtema", "titulo", "linguagem",
                                         "exercicio_id", "aluno_id", "caminho_codigo")}
            custo = (envelope or {}).get("total_cost_usd")
            return {"ok": True, "registro": {**r, "_meta": meta, "_modelo": modelo,
                                             "_prompt_sha": prompt_sha, "_custo_usd": custo}}
        except subprocess.TimeoutExpired:
            ultimo_erro = "timeout"
        except Exception as e:  # noqa: BLE001
            ultimo_erro = str(e)
            if "limit" in ultimo_erro.lower():  # limite de uso da assinatura
                time.sleep(120)
        time.sleep(5 * (t + 1))
    return {"ok": False, "registro": {"uid": item["uid"], "erro": ultimo_erro}}


# ---------- planilhas para revisão manual ----------
def prioridade(r):
    """Quanto maior, mais cedo o item aparece na planilha de revisão."""
    base = {"desvio": 3, "indeterminado": 2, "sem_desvio": 0}[r["veredito"]]
    if r["veredito"] == "desvio" and grupo_do_registro(r) in ("saida_fabricada", "misto"):
        base += 1
    return base * 10 + (1 if r["confianca"] == "baixa" else 0)


def gerar_planilhas(pasta):
    regs = carregar_resultados(pasta)
    if not regs:
        print("Nenhum resultado ainda.")
        return

    # preserva a revisão manual já feita (o arquivo pode ter sido salvo pelo Excel)
    manuais = {}
    arq_itens = os.path.join(pasta, "itens.csv")
    if os.path.exists(arq_itens):
        for linha in ler_csv_tolerante(arq_itens):
            if any((linha.get(c) or "").strip() for c in COLUNAS_MANUAIS):
                manuais[linha["uid"]] = {c: linha.get(c, "") for c in COLUNAS_MANUAIS}

    itens, desvios = [], []
    for r in regs.values():
        m = r.get("_meta", {})
        ds = r.get("desvios", [])
        exigs = r.get("exigencias", [])
        itens.append({
            "prioridade": prioridade(r), "uid": r["uid"], "disciplina": m.get("disciplina"),
            "categoria": m.get("categoria"), "subtema": m.get("subtema"), "titulo": m.get("titulo"),
            "linguagem": m.get("linguagem"), "veredito": r["veredito"], "confianca": r["confianca"],
            "n_desvios": len(ds), "tipos_desvio": "|".join(tipos_do_registro(r)),
            "grupo_desvio": grupo_do_registro(r),
            "exigencias_nao_cumpridas": "|".join(e["id"] for e in exigs
                                                 if e.get("status") == "nao_cumprida" and e.get("id")),
            "descricao_codigo": r.get("descricao_codigo", ""),
            "observacao_revisor": r.get("observacao_revisor", ""),
            "caminho_codigo": m.get("caminho_codigo"),
            **{c: manuais.get(r["uid"], {}).get(c, "") for c in COLUNAS_MANUAIS},
        })
        for d in ds:
            ex = next((e for e in exigs if e.get("id") == d.get("exigencia")), {})
            desvios.append({
                "uid": r["uid"], "disciplina": m.get("disciplina"), "subtema": m.get("subtema"),
                "titulo": m.get("titulo"), "exigencia": d.get("exigencia"),
                "trecho_enunciado": ex.get("trecho_enunciado", ""), "tipo": d.get("tipo"),
                "linhas": d.get("linhas"), "evidencia": d.get("evidencia"), "descricao": d.get("descricao"),
            })

    itens.sort(key=lambda x: (-x["prioridade"], x["uid"]))
    for nome, linhas in (("itens.csv", itens), ("desvios.csv", desvios)):
        if not linhas:
            continue
        with open(os.path.join(pasta, nome), "w", newline="", encoding="utf-8-sig") as f:
            w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()), delimiter=";")
            w.writeheader()
            w.writerows(linhas)

    cont = {v: sum(i["veredito"] == v for i in itens) for v in VEREDITOS}
    custo = sum((r.get("_custo_usd") or 0) for r in regs.values())
    print(f"\n{len(itens)} itens analisados: {cont['desvio']} com desvio, "
          f"{cont['indeterminado']} indeterminados, {cont['sem_desvio']} sem desvio")
    if custo:
        print(f"Custo equivalente informado pelo Claude Code: US$ {custo:.2f} "
              "(na assinatura não é cobrado; serve de referência para a API)")
    print(f"Planilhas: {pasta}/itens.csv e {pasta}/desvios.csv")


# ---------- principal ----------
def checar_versao(pasta, sha, modelo):
    """Impede misturar, numa mesma versão, resultados de prompts ou modelos diferentes."""
    arq = os.path.join(pasta, "execucao.json")
    if not os.path.exists(arq):
        return None
    ant = json.load(open(arq, encoding="utf-8"))
    if ant.get("prompt_sha256") != sha:
        sys.exit(f"O prompt mudou desde a última execução desta versão ({pasta}).\n"
                 "Salve o prompt novo com outro nome e use outra --versao (ex.: --versao v3), "
                 "para não misturar resultados de prompts diferentes.")
    if ant.get("modelo") != modelo:
        sys.exit(f"Esta versão foi rodada com o modelo '{ant.get('modelo')}' e agora você pediu '{modelo}'.\n"
                 "Use outra --versao para trocar de modelo.")
    return ant


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--amostra", default=os.path.join(RAIZ_PROJETO, "selecao", "amostra.jsonl"))
    ap.add_argument("--prompt", default=os.path.join(RAIZ_PROJETO, "prompt", "prompt_conformidade_V2.txt"))
    ap.add_argument("--versao", default="v2", help="nome desta versão do prompt (pasta de resultados)")
    ap.add_argument("--modelo", default="opus", help="alias do Claude Code: opus, sonnet, haiku...")
    ap.add_argument("--limite", type=int, default=0)
    ap.add_argument("--uids", default="", help="lista separada por vírgula")
    ap.add_argument("--paralelo", type=int, default=2, help="chamadas simultâneas (padrão 2)")
    ap.add_argument("--so-relatorio", action="store_true")
    args = ap.parse_args()

    pasta = pasta_da_versao(args.versao)
    os.makedirs(pasta, exist_ok=True)
    if args.so_relatorio:
        gerar_planilhas(pasta)
        return

    if os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ANTHROPIC_API_KEY está definida: o Claude Code cobraria na API. "
                 "Remova-a (PowerShell: Remove-Item Env:ANTHROPIC_API_KEY) e rode de novo.")
    exe = shutil.which("claude")
    if not exe:
        sys.exit("Comando 'claude' não encontrado. Instale o Claude Code e faça login.")

    modelo_prompt = open(args.prompt, encoding="utf-8").read()
    prompt_sha = hashlib.sha256(modelo_prompt.encode("utf-8")).hexdigest()
    anterior = checar_versao(pasta, prompt_sha, args.modelo)

    itens = [json.loads(l) for l in open(args.amostra, encoding="utf-8") if l.strip()]
    if args.uids:
        alvo = {u.strip() for u in args.uids.split(",")}
        itens = [i for i in itens if i["uid"] in alvo]
    if args.limite:
        itens = itens[: args.limite]

    feitos = set(carregar_resultados(pasta))
    pendentes = [i for i in itens if i["uid"] not in feitos]
    print(f"Versão {args.versao} | modelo {args.modelo} | {len(itens)} itens selecionados, "
          f"{len(itens) - len(pendentes)} já feitos, {len(pendentes)} pendentes.")

    agora = datetime.now(timezone.utc).isoformat()
    with open(os.path.join(pasta, "execucao.json"), "w", encoding="utf-8") as f:
        json.dump({"versao": args.versao, "ferramenta": "Claude Code (claude -p)", "modelo": args.modelo,
                   "prompt_arquivo": args.prompt, "prompt_sha256": prompt_sha, "system_prompt": SISTEMA,
                   "primeira_execucao_utc": (anterior or {}).get("primeira_execucao_utc", agora),
                   "execucoes_utc": (anterior or {}).get("execucoes_utc", []) + [agora],
                   "prompt": modelo_prompt}, f, ensure_ascii=False, indent=2)

    pasta_vazia = tempfile.mkdtemp(prefix="conformidade_")  # evita que o Claude Code leia arquivos do projeto
    arq_res, arq_err = os.path.join(pasta, "resultados.jsonl"), os.path.join(pasta, "erros.jsonl")
    ok = falhas = 0
    with ThreadPoolExecutor(max_workers=max(1, args.paralelo)) as pool:
        futuros = {pool.submit(processar, i, exe, args.modelo, modelo_prompt, prompt_sha, pasta_vazia): i
                   for i in pendentes}
        for n, fut in enumerate(as_completed(futuros), 1):
            res = fut.result()
            with trava, open(arq_res if res["ok"] else arq_err, "a", encoding="utf-8") as f:
                f.write(json.dumps(res["registro"], ensure_ascii=False) + "\n")
            ok += res["ok"]
            falhas += not res["ok"]
            r = res["registro"]
            status = f'{r.get("veredito")} (confianca {r.get("confianca")})' if res["ok"] else f'ERRO: {r["erro"][:80]}'
            print(f"[{n}/{len(pendentes)}] {r['uid']}: {status}")

    print(f"\nConcluído: {ok} ok, {falhas} com erro"
          + (f" (veja {arq_err} e rode de novo)" if falhas else ""))
    gerar_planilhas(pasta)


if __name__ == "__main__":
    main()