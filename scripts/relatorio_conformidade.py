"""
Relatórios da verificação de conformidade (use depois de verificar_conformidade.py).

1) TAMANHO DO PROBLEMA: proporção de códigos aceitos pelo juiz que NÃO cumprem o enunciado.
       python relatorio_conformidade.py --versao v2
   Para cada grupo (geral, disciplina, categoria, subtema e estrato) informa:
     - desvio / indeterminado / sem_desvio (contagens);
     - pct_desvio: só os desvios apontados (limite inferior);
     - pct_max: desvios + indeterminados (limite superior);
     - ic95: intervalo de confiança de Wilson para pct_desvio;
     - pct_pond: proporção PONDERADA pelo tamanho de cada estrato na população (veja abaixo).

   Por que ponderar: a amostra sorteia o mesmo número de códigos por categoria/subtema
   (rodízio), e não proporcional ao que existe no dataset. A proporção "crua" do conjunto
   inteiro, portanto, não representa a população. A ponderada usa selecao/resumo_categorias.csv
   (codigos_disponiveis por disciplina x categoria x subtema). Vale só para as categorias
   escolhidas, não para o dataset inteiro. A cobertura informa quanto da população entrou.

2) COMPARAR VERSÕES DO PROMPT (mesmos itens, prompts diferentes):
       python relatorio_conformidade.py --comparar v1 v2

3) CONCORDÂNCIA COM A SUA REVISÃO MANUAL:
       python relatorio_conformidade.py --versao v2 --gabarito
   Lê a coluna revisao_manual_desvio de conformidade/<versao>/itens.csv (sim | nao | indeterminado).
   Também aceita um CSV ';' com colunas uid;revisao_manual_desvio:  --gabarito meu_gabarito.csv

Saídas em conformidade/<versao>/ (ou conformidade/ para a comparação).
"""
import argparse
import csv
import math
import os
from collections import Counter, defaultdict

from verificar_conformidade import (RAIZ, RAIZ_PROJETO,carregar_resultados, grupo_do_registro, ler_csv_tolerante,
                                    pasta_da_versao, tipos_do_registro)

ROTULOS = ["desvio", "indeterminado", "sem_desvio"]
VEREDITO_ANTIGO = {"conforme": "sem_desvio", "nao_conforme": "desvio"}  # prompt v1
MANUAL = {"sim": "desvio", "desvio": "desvio", "nao": "sem_desvio", "não": "sem_desvio",
          "sem_desvio": "sem_desvio", "indeterminado": "indeterminado"}


# ---------- carga ----------
def carregar(versao):
    pasta = pasta_da_versao(versao)
    if not os.path.exists(os.path.join(pasta, "resultados.jsonl")) and versao == "v1" \
            and os.path.exists(os.path.join(RAIZ, "resultados.jsonl")):
        pasta = RAIZ  # layout antigo, antes de existir o --versao
    regs = carregar_resultados(pasta)
    if not regs:
        raise SystemExit(f"Sem resultados em {pasta}/resultados.jsonl")
    for r in regs.values():
        r["veredito"] = VEREDITO_ANTIGO.get(r["veredito"], r["veredito"])
    return regs, pasta


def carregar_populacao(caminho):
    """(disciplina, categoria, subtema) -> N (códigos disponíveis)."""
    if not os.path.exists(caminho):
        return None
    return {(l["disciplina"], l["categoria"], l["subtema"]): int(l["codigos_disponiveis"])
            for l in ler_csv_tolerante(caminho)}


# ---------- estatística ----------
def wilson(x, n, z=1.96):
    if n == 0:
        return 0.0, 0.0
    p = x / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def ponderado(estratos, chave_x):
    """Proporção ponderada pelo tamanho populacional N de cada estrato (aproximação normal,
    com correção de população finita). estratos: lista de dicts com N, n e contagens."""
    usados = [e for e in estratos if e["n"] > 0 and e["N"] > 0]
    if not usados:
        return None
    n_tot = sum(e["N"] for e in usados)
    p = sum(e["N"] * e[chave_x] / e["n"] for e in usados) / n_tot
    var = 0.0
    for e in usados:
        f = min(e["n"] / e["N"], 1.0)
        pt = (e[chave_x] + 1) / (e["n"] + 2)  # evita variância zero quando x = 0
        var += (e["N"] / n_tot) ** 2 * (1 - f) * pt * (1 - pt) / e["n"]
    se = math.sqrt(var)
    cobertura = n_tot / sum(e["N"] for e in estratos if e["N"] > 0)
    return p, max(0.0, p - 1.96 * se), min(1.0, p + 1.96 * se), cobertura


def kappa(pares):
    n = len(pares)
    cats = sorted({a for a, _ in pares} | {b for _, b in pares})
    po = sum(a == b for a, b in pares) / n
    pe = sum((sum(a == c for a, _ in pares) / n) * (sum(b == c for _, b in pares) / n) for c in cats)
    return (po - pe) / (1 - pe) if pe < 1 else 1.0


def pct(x):
    return "" if x is None else f"{100 * x:.1f}"


# ---------- 1) tamanho do problema ----------
def relatorio_tamanho(versao, arq_populacao):
    regs, pasta = carregar(versao)
    populacao = carregar_populacao(arq_populacao)

    estratos = defaultdict(lambda: Counter())
    for r in regs.values():
        m = r["_meta"]
        e = estratos[(m["disciplina"], m["categoria"], m["subtema"])]
        e["n"] += 1
        e[r["veredito"]] += 1

    def agrupar(chave):
        g = defaultdict(list)
        for k, c in estratos.items():
            g[chave(k)].append({"chave": k, "N": (populacao or {}).get(k, 0), "n": c["n"],
                                "x": c["desvio"], "xmax": c["desvio"] + c["indeterminado"],
                                "desvio": c["desvio"], "indeterminado": c["indeterminado"],
                                "sem_desvio": c["sem_desvio"]})
        return g

    niveis = [("geral", lambda k: "todos"), ("disciplina", lambda k: k[0]), ("categoria", lambda k: k[1]),
              ("subtema", lambda k: f"{k[1]}/{k[2]}"), ("estrato", lambda k: f"{k[0]} | {k[1]}/{k[2]}")]
    linhas = []
    for nivel, f in niveis:
        for nome, es in sorted(agrupar(f).items()):
            n = sum(e["n"] for e in es)
            d = sum(e["desvio"] for e in es)
            i = sum(e["indeterminado"] for e in es)
            lo, hi = wilson(d, n)
            linha = {"nivel": nivel, "grupo": nome, "n_analisados": n, "desvio": d, "indeterminado": i,
                     "sem_desvio": sum(e["sem_desvio"] for e in es),
                     "pct_desvio": pct(d / n), "pct_max": pct((d + i) / n),
                     "ic95_baixo": pct(lo), "ic95_alto": pct(hi),
                     "pct_pond": "", "ic95_pond_baixo": "", "ic95_pond_alto": "",
                     "pct_pond_max": "", "cobertura_populacao": ""}
            if populacao:
                pm = ponderado(es, "x")
                px = ponderado(es, "xmax")
                if pm:
                    linha.update(pct_pond=pct(pm[0]), ic95_pond_baixo=pct(pm[1]), ic95_pond_alto=pct(pm[2]),
                                 pct_pond_max=pct(px[0]), cobertura_populacao=pct(pm[3]))
            linhas.append(linha)

    arq = os.path.join(pasta, "tamanho_do_problema.csv")
    with open(arq, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.DictWriter(f, fieldnames=list(linhas[0].keys()), delimiter=";")
        w.writeheader()
        w.writerows(linhas)

    # tipos de desvio (sobre todos os itens analisados)
    n_total = len(regs)
    por_tipo, por_grupo = Counter(), Counter()
    for r in regs.values():
        for t in tipos_do_registro(r):
            por_tipo[t] += 1
        g = grupo_do_registro(r)
        if g:
            por_grupo[g] += 1
    arq_t = os.path.join(pasta, "tipos_de_desvio.csv")
    with open(arq_t, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["tipo_ou_grupo", "itens", "pct_dos_analisados"])
        for k, v in sorted(por_grupo.items()):
            w.writerow([f"grupo:{k}", v, pct(v / n_total)])
        for k, v in por_tipo.most_common():
            w.writerow([k, v, pct(v / n_total)])

    # ---- resumo no terminal ----
    print(f"\nVersão {versao}: {n_total} códigos analisados (aceitos pelo juiz)\n")
    cab = f"{'grupo':<34}{'n':>5}{'desvio':>8}{'indet.':>8}{'%desvio':>9}{'IC95':>15}{'%pond':>8}"
    print(cab)
    print("-" * len(cab))
    for l in linhas:
        if l["nivel"] in ("geral", "disciplina", "categoria"):
            ic = f"[{l['ic95_baixo']}-{l['ic95_alto']}]"
            print(f"{l['grupo']:<34}{l['n_analisados']:>5}{l['desvio']:>8}{l['indeterminado']:>8}"
                  f"{l['pct_desvio']:>9}{ic:>15}{l['pct_pond']:>8}")
    geral = linhas[0]
    print(f"\nLimite superior (desvios + indeterminados): {geral['pct_max']}%")
    if populacao:
        print(f"Ponderado pela população das categorias escolhidas: {geral['pct_pond']}% "
              f"[{geral['ic95_pond_baixo']}-{geral['ic95_pond_alto']}], cobertura {geral['cobertura_populacao']}% da população")
    else:
        print("Sem ponderação: selecao/resumo_categorias.csv não encontrado (use --populacao).")
    if por_tipo:
        print("\nTipos de desvio (itens): " + ", ".join(f"{k}={v}" for k, v in por_tipo.most_common()))
    print(f"\nTabelas completas: {arq} e {arq_t}")
    print("Obs.: a proporção é estimada pela LLM. Valide com sua revisão manual (--gabarito) antes de citar.")


# ---------- 2) comparação entre versões ----------
def comparar(v1, v2):
    r1, _ = carregar(v1)
    r2, _ = carregar(v2)
    comuns = sorted(set(r1) & set(r2))
    if not comuns:
        raise SystemExit("Nenhum item em comum entre as duas versões.")
    pares = [(r1[u]["veredito"], r2[u]["veredito"]) for u in comuns]
    iguais = sum(a == b for a, b in pares)
    print(f"\n{len(comuns)} itens em comum entre {v1} e {v2}")
    print(f"Concordância: {pct(iguais / len(comuns))}% | kappa de Cohen: {kappa(pares):.2f}\n")
    tab = Counter(pares)
    print(f"{v1} \\ {v2}".ljust(18) + "".join(f"{c:>15}" for c in ROTULOS))
    for a in ROTULOS:
        print(a.ljust(18) + "".join(f"{tab[(a, b)]:>15}" for b in ROTULOS))

    arq = os.path.join(RAIZ, f"comparacao_{v1}_{v2}.csv")
    with open(arq, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["uid", "disciplina", "subtema", "titulo", f"veredito_{v1}", f"veredito_{v2}",
                    f"tipos_{v1}", f"tipos_{v2}", f"descricao_desvios_{v1}", f"descricao_desvios_{v2}"])
        for u in comuns:
            a, b = r1[u], r2[u]
            if a["veredito"] != b["veredito"] or tipos_do_registro(a) != tipos_do_registro(b):
                m = a["_meta"]
                w.writerow([u, m["disciplina"], m["subtema"], m["titulo"], a["veredito"], b["veredito"],
                            "|".join(tipos_do_registro(a)), "|".join(tipos_do_registro(b)),
                            " / ".join(d.get("descricao", "") for d in a.get("desvios", [])),
                            " / ".join(d.get("descricao", "") for d in b.get("desvios", []))])
    print(f"\nItens que mudaram (veredito ou tipo): {arq}")


# ---------- 3) concordância com a revisão manual ----------
def gabarito(versao, origem):
    regs, pasta = carregar(versao)
    arq = os.path.join(pasta, "itens.csv") if origem == "auto" else origem
    if not os.path.exists(arq):
        raise SystemExit(f"Arquivo não encontrado: {arq}")
    manual = {}
    for l in ler_csv_tolerante(arq):
        valor = (l.get("revisao_manual_desvio") or l.get("desvio_manual") or "").strip().lower()
        if valor:
            if valor not in MANUAL:
                raise SystemExit(f"Valor inválido '{valor}' em {l.get('uid')}: use sim, nao ou indeterminado.")
            manual[l["uid"]] = MANUAL[valor]
    uids = sorted(u for u in manual if u in regs)
    if not uids:
        raise SystemExit("Nenhum item revisado manualmente (preencha revisao_manual_desvio em itens.csv).")

    pares = [(manual[u], regs[u]["veredito"]) for u in uids]  # (referência, LLM)
    print(f"\n{len(uids)} itens com revisão manual (versão {versao})")
    print("linhas = sua revisão | colunas = veredito da LLM\n")
    tab = Counter(pares)
    print("".ljust(18) + "".join(f"{c:>15}" for c in ROTULOS))
    for a in ROTULOS:
        print(a.ljust(18) + "".join(f"{tab[(a, b)]:>15}" for b in ROTULOS))

    tp = tab[("desvio", "desvio")]
    fp = sum(v for (a, b), v in tab.items() if b == "desvio" and a != "desvio")
    fn = sum(v for (a, b), v in tab.items() if a == "desvio" and b != "desvio")
    prec = tp / (tp + fp) if tp + fp else None
    rev = tp / (tp + fn) if tp + fn else None
    f1 = 2 * prec * rev / (prec + rev) if prec and rev else None
    print(f"\nConcordância: {pct(sum(a == b for a, b in pares) / len(pares))}% | kappa: {kappa(pares):.2f}")
    print(f"Para 'desvio': precisão {pct(prec)}% | revocação {pct(rev)}% | F1 {pct(f1)}%")
    print("(precisão = dos que a LLM apontou, quantos você confirmou; "
          "revocação = dos que você considera desvio, quantos a LLM apontou)")

    saida = os.path.join(pasta, "desacordos.csv")
    with open(saida, "w", newline="", encoding="utf-8-sig") as f:
        w = csv.writer(f, delimiter=";")
        w.writerow(["uid", "titulo", "revisao_manual", "veredito_llm", "tipos_llm", "descricao_desvios_llm",
                    "observacao_revisor_llm"])
        for u in uids:
            if manual[u] != regs[u]["veredito"]:
                r = regs[u]
                w.writerow([u, r["_meta"]["titulo"], manual[u], r["veredito"], "|".join(tipos_do_registro(r)),
                            " / ".join(d.get("descricao", "") for d in r.get("desvios", [])),
                            r.get("observacao_revisor", "")])
    print(f"\nDesacordos para analisar e ajustar o prompt: {saida}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--versao", default="v2")
    ap.add_argument("--comparar", nargs=2, metavar=("VERSAO_A", "VERSAO_B"))
    ap.add_argument("--gabarito", nargs="?", const="auto", default=None)
    ap.add_argument("--populacao", default=os.path.join(RAIZ_PROJETO, "selecao", "resumo_categorias.csv"))
    args = ap.parse_args()
    if args.comparar:
        comparar(*args.comparar)
    elif args.gabarito:
        gabarito(args.versao, args.gabarito)
    else:
        relatorio_tamanho(args.versao, args.populacao)


if __name__ == "__main__":
    main()