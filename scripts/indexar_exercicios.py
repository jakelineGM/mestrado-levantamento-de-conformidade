"""
Gera um índice compacto do cb-dataset (CodeBench/CodeMeistre) para triagem com LLM.

Uso (de qualquer pasta; o dataset é lido de ../cb-dataset ou da variável CB_DATASET):
    python scripts/indexar_exercicios.py

Saídas (em classificacao/):
    indice_exercicios.csv     -> uma linha por exercício (para abrir no Excel/pandas)
    enunciados_unicos.jsonl   -> um registro por enunciado ÚNICO (é isso que vai para a LLM)
"""
import csv
import glob
import hashlib
import html
import json
import os
import re
from collections import defaultdict

# Raiz do projeto (pasta acima de scripts/) e do dataset (irmão: ../cb-dataset, ou CB_DATASET).
RAIZ_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET = os.path.abspath(os.environ.get("CB_DATASET") or os.path.join(os.path.dirname(RAIZ_PROJETO), "cb-dataset"))
SAIDA = os.path.join(RAIZ_PROJETO, "classificacao")

def ler_data_txt(caminho):
    dados = {}
    if os.path.exists(caminho):
        with open(caminho, encoding="utf-8", errors="ignore") as f:
            for linha in f:
                if ":" in linha:
                    k, v = linha.split(":", 1)
                    dados[k.strip()] = v.strip()
    return dados


def html_para_texto(caminho):
    with open(caminho, encoding="utf-8", errors="ignore") as f:
        bruto = f.read()
    texto = re.sub(r"<[^>]+>", " ", bruto)
    return re.sub(r"\s+", " ", html.unescape(texto)).strip()


linhas = []
if not os.path.isdir(DATASET):
    raise SystemExit(f"Dataset não encontrado em {DATASET}. Defina CB_DATASET com o caminho correto.")
os.makedirs(SAIDA, exist_ok=True)

for st in sorted(glob.glob(os.path.join(DATASET, "*", "*", "*", "*", "statement.html"))):
    # "pasta" fica relativa ao dataset (é o que vai para a coluna "caminho" do índice)
    pasta = os.path.relpath(os.path.dirname(st), DATASET)
    curso, turma, avaliacao, exercicio = pasta.split(os.sep)
    abs_pasta = os.path.join(DATASET, pasta)
    ex = ler_data_txt(os.path.join(abs_pasta, "data.txt"))
    av = ler_data_txt(os.path.join(DATASET, curso, turma, avaliacao, "data.txt"))
    tu = ler_data_txt(os.path.join(DATASET, curso, turma, "data.txt"))
    cu = ler_data_txt(os.path.join(DATASET, curso, "data.txt"))
    alunos = [d for d in os.listdir(abs_pasta) if d.isdigit() and os.path.isdir(os.path.join(abs_pasta, d))]
    enunciado = html_para_texto(st)
    linhas.append({
        "caminho": pasta,
        "disciplina": cu.get("name", curso),
        "turma": f'{tu.get("year", "")}.{tu.get("semester", "")}',
        "avaliacao": av.get("title", ""),
        "linguagem": av.get("programmingLanguage", ""),
        "titulo": ex.get("title", ""),
        "n_alunos": len(alunos),
        "hash_enunciado": hashlib.md5(enunciado.encode()).hexdigest()[:10],
        "enunciado": enunciado,
    })

with open(os.path.join(SAIDA, "indice_exercicios.csv"), "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()))
    w.writeheader()
    w.writerows(linhas)

# Agrupa exercícios repetidos entre turmas: a LLM só precisa ver cada enunciado uma vez.
grupos = defaultdict(list)
for l in linhas:
    grupos[l["hash_enunciado"]].append(l)

with open(os.path.join(SAIDA, "enunciados_unicos.jsonl"), "w", encoding="utf-8") as f:
    for h, itens in grupos.items():
        f.write(json.dumps({
            "id": h,
            "titulo": itens[0]["titulo"],
            "disciplina": itens[0]["disciplina"],
            "linguagem": itens[0]["linguagem"],
            "ocorrencias": len(itens),
            "total_alunos": sum(i["n_alunos"] for i in itens),
            "enunciado": itens[0]["enunciado"][:3000],
        }, ensure_ascii=False) + "\n")

print(f"{len(linhas)} exercícios -> {len(grupos)} enunciados únicos")
print(f"{sum(l['n_alunos'] for l in linhas)} códigos de alunos no total")