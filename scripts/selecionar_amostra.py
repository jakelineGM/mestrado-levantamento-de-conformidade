"""
Sorteia 200 códigos de alunos por disciplina (AED, AED I, AED II) do cb-dataset,
alternando entre as categorias escolhidas (round-robin), e organiza tudo para a
etapa seguinte (verificação de conformidade enunciado x código com LLM).

Regra de seleção (por disciplina):
  - As categorias são percorridas na ordem do arquivo --categorias.
  - Em cada vez, sorteia-se UMA questão (exercício + código de um aluno) da categoria da vez.
  - Dentro da categoria, os subtemas também se alternam: a cada vez que a categoria é
    chamada, usa-se o próximo subtema (em ordem aleatória a cada rodada). Assim todos os
    subtemas mantidos aparecem antes de qualquer um se repetir.
  - Categoria (ou subtema) sem questões, ou já esgotado, é pulado.
  - Ao passar da última categoria, volta para a primeira, até completar --n (padrão 200).
  - Dentro de um subtema, os exercícios são sorteados sem repetição até todos terem
    sido usados uma vez; só então um exercício pode aparecer de novo (com outro aluno).
    Isso evita que um único exercício com muitos alunos domine o subtema.
  - Um mesmo código (exercício + aluno) nunca é sorteado duas vezes.
  - Semente fixa (--seed) => o sorteio é reproduzível.

Uso (de qualquer pasta; o dataset é lido de ../cb-dataset ou da variável CB_DATASET):
    python scripts/selecionar_amostra.py --categorias categorias.txt
    python scripts/selecionar_amostra.py --categorias categorias.txt --n 200 --seed 42

O arquivo --categorias define QUAIS pares categoria/subtema entram e em que ORDEM as
categorias são percorridas (ordem da primeira aparição no arquivo). Pode ser:
  a) .csv com colunas "categoria" e "subtema" (ex.: o resumo_por_categoria.csv filtrado);
  b) .csv só com "categoria" (todos os subtemas da categoria entram);
  c) a própria classificacao.csv filtrada (com coluna "id": só esses enunciados entram);
  d) .txt com uma linha por categoria, ou "categoria;subtema" por linha.

Saídas (pasta selecao/):
  amostra.csv              -> uma linha por código sorteado (sem textos longos)
  amostra.jsonl            -> idem + enunciado, código e casos de teste (entrada da próxima etapa)
  resumo_categorias.csv    -> por disciplina x categoria: exercícios, códigos disponíveis, sorteados
  resumo.md                -> o mesmo resumo em texto legível
  parametros.json          -> semente, categorias, data (para a metodologia)
  <DISCIPLINA>/<ordem>_<categoria>_<exercicio>_<aluno>/  -> enunciado.md, código, test-cases/
"""
import argparse
import csv
import glob
import html
import json
import os
import random
import re
import shutil
from collections import OrderedDict, defaultdict
from datetime import datetime, timezone

# Raiz do projeto (pasta acima de scripts/) e do dataset (irmão: ../cb-dataset, ou CB_DATASET).
RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = os.path.abspath(os.environ.get("CB_DATASET") or os.path.join(os.path.dirname(RAIZ_PROJETO), "cb-dataset"))

EXT_CODIGO = {".c", ".h", ".py", ".go", ".cpp", ".hpp", ".java", ".js"}
SIGLAS = {
    "Algoritmos e Estruturas de Dados": "AED",
    "Algoritmos e Estruturas de Dados I": "AED1",
    "Algoritmos e Estruturas de Dados II": "AED2",
}


def ler_kv(caminho):
    d = {}
    if os.path.exists(caminho):
        for linha in open(caminho, encoding="utf-8", errors="ignore"):
            if ":" in linha:
                k, v = linha.split(":", 1)
                d[k.strip()] = v.strip()
    return d


def html_para_texto(caminho):
    if not os.path.exists(caminho):
        return ""
    bruto = open(caminho, encoding="utf-8", errors="ignore").read()
    bruto = re.sub(r"<\s*(br|/p|/li|/h\d|/pre)\s*/?>", "\n", bruto, flags=re.I)
    texto = html.unescape(re.sub(r"<[^>]+>", "", bruto))
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", texto)).strip()


def ler_csv(caminho):
    with open(caminho, encoding="utf-8") as f:
        amostra = f.read(4096)
        f.seek(0)
        sep = ";" if amostra.count(";") >= amostra.count(",") else ","
        return list(csv.DictReader(f, delimiter=sep))


def carregar_categorias(caminho):
    """Devolve (OrderedDict categoria -> set de subtemas ou None = todos, ids permitidos ou None)."""
    cats = OrderedDict()
    ids = None
    if caminho.lower().endswith(".txt"):
        for l in open(caminho, encoding="utf-8"):
            l = l.strip()
            if not l or l.startswith("#"):
                continue
            partes = [p.strip() for p in re.split(r"[;,]", l)]
            cat, sub = partes[0], (partes[1] if len(partes) > 1 and partes[1] else None)
            cats.setdefault(cat, set())
            if sub is None:
                cats[cat] = None
            elif cats[cat] is not None:
                cats[cat].add(sub)
    else:
        linhas = ler_csv(caminho)
        tem_sub = "subtema" in linhas[0]
        for l in linhas:
            cat = l["categoria"].strip()
            if not cat:
                continue
            cats.setdefault(cat, set() if tem_sub else None)
            if tem_sub and l["subtema"].strip():
                cats[cat].add(l["subtema"].strip())
        if "id" in linhas[0]:
            ids = {l["id"] for l in linhas}
    return OrderedDict((c, (None if s is None or not s else s)) for c, s in cats.items()), ids


def arquivos_de_codigo(pasta_aluno):
    return sorted(
        os.path.relpath(p, pasta_aluno)
        for p in glob.glob(os.path.join(pasta_aluno, "**", "*"), recursive=True)
        if os.path.isfile(p) and os.path.splitext(p)[1].lower() in EXT_CODIGO
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--categorias", required=True)
    ap.add_argument("--classificacao", default=os.path.join(RAIZ_PROJETO, "classificacao", "classificacao.csv"))
    ap.add_argument("--indice", default=os.path.join(RAIZ_PROJETO, "classificacao", "indice_exercicios.csv"))
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--saida", default=os.path.join(RAIZ_PROJETO, "selecao"))
    ap.add_argument("--sem-pastas", action="store_true", help="não copia código/enunciado para subpastas")
    args = ap.parse_args()

    permitidas, ids_permitidos = carregar_categorias(args.categorias)
    rotulos = list(permitidas)
    classif = {r["id"]: r for r in ler_csv(args.classificacao)}
    if ids_permitidos is not None:
        classif = {k: v for k, v in classif.items() if k in ids_permitidos}

    def aceito(c):
        subs = permitidas.get(c["categoria"], False)
        return subs is not False and (subs is None or c["subtema"] in subs)

    pares_class = {(c["categoria"], c["subtema"]) for c in classif.values()}
    for cat, subs in permitidas.items():
        for sub in (subs or []):
            if (cat, sub) not in pares_class:
                print(f"AVISO: {cat}/{sub} não tem nenhum enunciado na classificação.")

    # Universo: disciplina -> categoria -> subtema -> [exercícios com seus alunos válidos]
    indice = ler_csv(args.indice)
    for ex in indice:  # índices gerados no Windows vêm com "\\"; padroniza para "/"
        ex["caminho"] = ex["caminho"].replace("\\", "/")
    universo = defaultdict(lambda: defaultdict(lambda: defaultdict(list)))
    nomes_disc = {}
    for ex in sorted(indice, key=lambda e: e["caminho"]):
        c = classif.get(ex["hash_enunciado"])
        if not c or not aceito(c):
            continue
        pasta = os.path.join(DATASET, ex["caminho"].replace("/", os.sep))
        alunos = sorted(
            a for a in os.listdir(pasta)
            if a.isdigit() and os.path.isdir(os.path.join(pasta, a)) and arquivos_de_codigo(os.path.join(pasta, a))
        )
        curso = ex["caminho"].split("/")[0]
        nomes_disc[curso] = ex["disciplina"]
        universo[curso][c["categoria"]][c["subtema"]].append({"ex": ex, "class": c, "alunos": alunos})

    if len(universo) > len(SIGLAS):
        raise SystemExit(f"ERRO: {len(universo)} disciplinas encontradas (esperado até {len(SIGLAS)}). "
                         "Verifique a coluna 'caminho' do indice_exercicios.csv.")

    rng = random.Random(args.seed)
    os.makedirs(args.saida, exist_ok=True)
    amostra, resumo = [], []

    for curso in sorted(universo, key=lambda k: SIGLAS.get(nomes_disc[k], nomes_disc[k])):
        sigla = SIGLAS.get(nomes_disc[curso], curso)
        estado = {}
        for rot in rotulos:
            subs = {}
            for sub, exs in sorted(universo[curso].get(rot, {}).items()):
                subs[sub] = {"exs": exs, "restantes": {id(e): list(e["alunos"]) for e in exs}, "fila": []}
            estado[rot] = {"subs": subs, "fila_subs": []}

        def vivos(st_sub):
            return [e for e in st_sub["exs"] if st_sub["restantes"][id(e)]]

        def sortear(rot):
            st = estado[rot]
            subs_vivos = [s_ for s_, v in st["subs"].items() if vivos(v)]
            if not subs_vivos:
                return None
            st["fila_subs"] = [s_ for s_ in st["fila_subs"] if s_ in subs_vivos]
            if not st["fila_subs"]:  # nova rodada de subtemas, em ordem aleatória
                st["fila_subs"] = subs_vivos[:]
                rng.shuffle(st["fila_subs"])
            sub = st["fila_subs"].pop(0)
            ss = st["subs"][sub]
            ss["fila"] = [e for e in ss["fila"] if ss["restantes"][id(e)]]
            if not ss["fila"]:  # nova rodada de exercícios, em ordem aleatória
                ss["fila"] = vivos(ss)
                rng.shuffle(ss["fila"])
            e = ss["fila"].pop(0)
            alunos = ss["restantes"][id(e)]
            aluno = alunos.pop(rng.randrange(len(alunos)))
            return e, aluno

        selecionados = []
        while len(selecionados) < args.n:
            avancou = False
            for rot in rotulos:
                if len(selecionados) >= args.n:
                    break
                r = sortear(rot)
                if r:
                    selecionados.append((rot, *r))
                    avancou = True
            if not avancou:
                print(f"AVISO: {sigla} esgotou todas as categorias com {len(selecionados)} códigos (meta {args.n}).")
                break

        cont = defaultdict(int)
        for ordem, (rot, e, aluno) in enumerate(selecionados, 1):
            ex, c = e["ex"], e["class"]
            cont[(c["categoria"], c["subtema"])] += 1
            pasta_ex = os.path.join(DATASET, ex["caminho"].replace("/", os.sep))
            pasta_aluno = os.path.join(pasta_ex, aluno)
            arqs = arquivos_de_codigo(pasta_aluno)
            codigo = "\n\n".join(
                f"// ===== {a} =====\n" + open(os.path.join(pasta_aluno, a), encoding="utf-8", errors="ignore").read()
                for a in arqs
            )
            casos = []
            for inp in sorted(glob.glob(os.path.join(pasta_ex, "test-cases", "*.input.txt")),
                              key=lambda p: int(os.path.basename(p).split(".")[0])):
                out = inp.replace(".input.txt", ".output.txt")
                casos.append({
                    "entrada": open(inp, encoding="utf-8", errors="ignore").read(),
                    "saida": open(out, encoding="utf-8", errors="ignore").read() if os.path.exists(out) else "",
                })
            exercicio_id = ex["caminho"].split("/")[-1]
            uid = f"{sigla}-{ordem:03d}"
            reg = {
                "uid": uid, "disciplina": sigla, "ordem": ordem,
                "categoria": c["categoria"], "subtema": c["subtema"],
                "categoria_secundaria": c.get("categoria_secundaria", ""),
                "titulo": ex["titulo"], "linguagem": ex["linguagem"],
                "turma": ex["turma"], "avaliacao": ex["avaliacao"],
                "exercicio_id": exercicio_id, "aluno_id": aluno,
                "hash_enunciado": ex["hash_enunciado"],
                "caminho_exercicio": ex["caminho"],
                "caminho_codigo": f'{ex["caminho"]}/{aluno}',
                "arquivos_codigo": "|".join(arqs),
                "n_casos_teste": len(casos),
            }
            amostra.append({**reg, "enunciado": html_para_texto(os.path.join(pasta_ex, "statement.html")),
                            "dicas": html_para_texto(os.path.join(pasta_ex, "tips.html")),
                            "codigo": codigo, "casos_teste": casos})

            if not args.sem_pastas:
                destino = os.path.join(args.saida, sigla, f"{ordem:03d}_{c['categoria']}-{c['subtema']}_{exercicio_id}_{aluno}")
                os.makedirs(os.path.join(destino, "codigo"), exist_ok=True)
                with open(os.path.join(destino, "enunciado.md"), "w", encoding="utf-8") as f:
                    f.write(f"# {ex['titulo']}\n\n{amostra[-1]['enunciado']}\n")
                    if amostra[-1]["dicas"]:
                        f.write(f"\n## Dicas\n\n{amostra[-1]['dicas']}\n")
                for a in arqs:
                    os.makedirs(os.path.dirname(os.path.join(destino, "codigo", a)), exist_ok=True)
                    shutil.copy2(os.path.join(pasta_aluno, a), os.path.join(destino, "codigo", a))
                if os.path.isdir(os.path.join(pasta_ex, "test-cases")):
                    shutil.copytree(os.path.join(pasta_ex, "test-cases"), os.path.join(destino, "test-cases"),
                                    dirs_exist_ok=True)
                with open(os.path.join(destino, "metadados.json"), "w", encoding="utf-8") as f:
                    json.dump(reg, f, ensure_ascii=False, indent=2)

        for rot in rotulos:
            subs_resumo = sorted(set(universo[curso].get(rot, {})) | set(permitidas[rot] or []))
            for sub in subs_resumo:
                exs = universo[curso].get(rot, {}).get(sub, [])
                resumo.append({
                    "disciplina": sigla, "categoria": rot, "subtema": sub,
                    "exercicios_disponiveis": len(exs),
                    "enunciados_unicos": len({e["ex"]["hash_enunciado"] for e in exs}),
                    "codigos_disponiveis": sum(len(e["alunos"]) for e in exs),
                    "codigos_sorteados": cont.get((rot, sub), 0),
                    "exercicios_distintos_sorteados": len({e["ex"]["caminho"] for _, e, _ in selecionados
                                                           if e["class"]["subtema"] == sub
                                                           and e["class"]["categoria"] == rot}),
                })

    # ---- Gravação ----
    campos_csv = [k for k in amostra[0] if k not in ("enunciado", "dicas", "codigo", "casos_teste")]
    with open(os.path.join(args.saida, "amostra.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=campos_csv, delimiter=";", extrasaction="ignore")
        w.writeheader()
        w.writerows(amostra)
    with open(os.path.join(args.saida, "amostra.jsonl"), "w", encoding="utf-8") as f:
        for r in amostra:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    with open(os.path.join(args.saida, "resumo_categorias.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(resumo[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(resumo)

    linhas_md = [f"# Resumo da amostra\n\nSemente: {args.seed} | Meta por disciplina: {args.n} | "
                 f"Ordem das categorias: {', '.join(rotulos)}\n"]
    for sigla in OrderedDict.fromkeys(r["disciplina"] for r in resumo):
        rs = [r for r in resumo if r["disciplina"] == sigla]
        total = sum(r["codigos_sorteados"] for r in rs)
        linhas_md.append(f"\n## {sigla} — {total} códigos sorteados\n")
        linhas_md.append("### Por categoria\n")
        linhas_md.append("| categoria | exercícios | códigos disponíveis | sorteados |")
        linhas_md.append("|---|---:|---:|---:|")
        for cat in rotulos:
            rc = [r for r in rs if r["categoria"] == cat]
            linhas_md.append(f"| {cat} | {sum(r['exercicios_disponiveis'] for r in rc)} | "
                             f"{sum(r['codigos_disponiveis'] for r in rc)} | {sum(r['codigos_sorteados'] for r in rc)} |")
        linhas_md.append("\n### Por subtema\n")
        linhas_md.append("| categoria | subtema | exercícios | enunciados únicos | códigos disponíveis | sorteados | exercícios distintos sorteados |")
        linhas_md.append("|---|---|---:|---:|---:|---:|---:|")
        for r in rs:
            linhas_md.append(f"| {r['categoria']} | {r['subtema']} | {r['exercicios_disponiveis']} | {r['enunciados_unicos']} | "
                             f"{r['codigos_disponiveis']} | {r['codigos_sorteados']} | {r['exercicios_distintos_sorteados']} |")
    open(os.path.join(args.saida, "resumo.md"), "w", encoding="utf-8").write("\n".join(linhas_md) + "\n")

    with open(os.path.join(args.saida, "parametros.json"), "w", encoding="utf-8") as f:
        json.dump({"data_utc": datetime.now(timezone.utc).isoformat(), "seed": args.seed, "n_por_disciplina": args.n,
                   "categorias_em_ordem": rotulos,
                   "subtemas_permitidos": {c: (sorted(v) if v else "todos") for c, v in permitidas.items()}, "arquivo_categorias": args.categorias,
                   "arquivo_classificacao": args.classificacao}, f, ensure_ascii=False, indent=2)

    print("\n".join(linhas_md))


if __name__ == "__main__":
    main()