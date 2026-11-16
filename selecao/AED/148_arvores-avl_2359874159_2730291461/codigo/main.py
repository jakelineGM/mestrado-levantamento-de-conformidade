def cria_nodo(valor):
  return {"valor": valor, "esq": None, "dir": None, "h": 1}

def insere_bst(raiz, valor):
  """ Insere valor na árvore binária de busca, retornando a nova raiz. """
  if raiz is None:
    return cria_nodo(valor)

  if valor < raiz["valor"]:
    raiz["esq"] = insere_bst(raiz["esq"], valor)
  else:
    raiz["dir"] = insere_bst(raiz["dir"], valor)

  atualiza_altura(raiz)
  return raiz

def atualiza_altura(no):
  if no is None:
    return
  no["h"] = 1 + max(altura(no["esq"]), altura(no["dir"]))

def altura(no):
  if no is None:
    return 0
  return no["h"]

def rotacao_rr(T):
  if T is None or T["dir"] is None:
    return T

  nova_raiz = T["dir"]
  T["dir"] = nova_raiz["esq"]
  nova_raiz["esq"] = T
  return nova_raiz

def rotacao_ll(T):
  if T is None or T["esq"] is None:
    return T

  L = T["esq"]
  B = L["dir"]

  L["dir"] = T
  T["esq"] = B

  atualiza_altura(T)
  atualiza_altura(L)

  return L

def pre_ordem(raiz, visita):
  if raiz is None:
    return
  visita.append(raiz["valor"])
  pre_ordem(raiz["esq"], visita)
  pre_ordem(raiz["dir"], visita)

def in_ordem(raiz, visita):
  if raiz is None:
    return
  in_ordem(raiz["esq"], visita)
  visita.append(raiz["valor"])
  in_ordem(raiz["dir"], visita)

def pos_ordem(raiz, visita):
  if raiz is None:
    return
  pos_ordem(raiz["esq"], visita)
  pos_ordem(raiz["dir"], visita)
  visita.append(raiz["valor"])

def fator_balanceamento(raiz):
  if raiz is None:
    return 0
  h = altura(raiz["dir"]) - altura(raiz["esq"])
  return h

def main():
  num_arvore = 1
  primeiro = True

  while True:
    linha = input().strip()
    if not linha:
      continue

    valores = eval(linha)

    if valores == []:
      break

    raiz = None
    for v in valores:
      raiz = insere_bst(raiz, v)

    raiz = rotacao_ll(raiz)

    h = altura(raiz)
    fb = fator_balanceamento(raiz)
    
    pre = []
    pos = []

    pre_ordem(raiz, pre)
    pos_ordem(raiz, pos)

    print(f"Arvore {num_arvore}")
    print(f"h: {h}")
    print(f"fb: {fb}")
    print("pre:", " ".join(map(str, pre)))
    print("pos:", " ".join(map(str, pos)))
    print()

    num_arvore += 1

if __name__ == "__main__":
  main()