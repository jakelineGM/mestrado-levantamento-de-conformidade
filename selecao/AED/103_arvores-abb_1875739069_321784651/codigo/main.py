def inserir(raiz, chave):
  if raiz is None:
    return {"valor": chave, "esq": None, "dir": None}
  if chave < raiz["valor"]:
    raiz["esq"] = inserir(raiz["esq"], chave)
  else:
    raiz["dir"] = inserir(raiz["dir"], chave)
  return raiz


def pre_ordem(no, visita):
  if no is None:
    return
  visita.append(no["valor"])
  pre_ordem(no["esq"], visita)
  pre_ordem(no["dir"], visita)


def in_ordem(no, visita):
  if no is None:
    return
  in_ordem(no["esq"], visita)
  visita.append(no["valor"])
  in_ordem(no["dir"], visita)

def pos_ordem(no, visita):
  if no is None:
    return
  pos_ordem(no["esq"], visita)
  pos_ordem(no["dir"], visita)
  visita.append(no["valor"])

def main():
  arvore_saida = []
  indice = 1

  while True:
    try:
      linha = input().strip()
    except EOFError:
      break

    if not linha:
      continue

    valores = eval(linha)

    if valores == []:
      break

    raiz = None
    for v in valores:
      raiz = inserir(raiz, v)

    pre = []
    ino = []
    pos = []
    pre_ordem(raiz, pre)
    in_ordem(raiz, ino)
    pos_ordem(raiz, pos)

    bloco = [
      f"Arvore {indice}",
      "Pre-ordem: " + " ".join(map(str, pre)),
      "In-ordem: " + " ".join(map(str, ino)),
      "Pos-ordem: " + " ".join(map(str, pos))
    ]
    arvore_saida.append("\n".join(bloco))
    indice += 1

  if arvore_saida:
    print("\n\n".join(arvore_saida))

if __name__ == "__main__":
    main()