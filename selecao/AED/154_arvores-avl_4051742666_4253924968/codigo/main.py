def busca_bst(arvore, chave):
  atual = arvore
  while atual is not None:
    if chave == atual['valor']:
      return True
    elif chave < atual['valor']:
      atual = atual['esq']
    else:
      atual = atual['dir']
  return False

def insere_bst(raiz, valor):
  if raiz is None:
    return{'valor': valor, 'esq': None, 'dir': None}
  if valor < raiz['valor']:
    raiz['esq'] = insere_bst(raiz['esq'], valor)
  else:
    raiz['dir'] = insere_bst(raiz['dir'], valor)
  return raiz

def rotacao_esquerda(no):
  if no is None or no['dir'] is None:
    return no
  y = no['dir']
  no['dir'] = y['esq']
  y['esq'] = no
  return y

# Leitura árvore
def pre_ordem(no, visita):
  if no is not None:
    visita.append(no['valor'])
    pre_ordem(no['esq'], visita)
    pre_ordem(no['dir'], visita)

def in_ordem(no, visita):
  if no is not None:
    in_ordem(no['esq'], visita)
    visita.append(no['valor'])
    in_ordem(no['dir'], visita)

def pos_ordem(no, visita):
  if no is not None:
    pos_ordem(no['esq'], visita)
    pos_ordem(no['dir'], visita)
    visita.append(no['valor'])

arvore_num = 1

while True:
  linha = input().strip()
  if linha == "":
    continue
  valores = eval(linha)
  if valores == []:
    break
  raiz = None
  for v in valores:
    raiz = insere_bst(raiz, v)
  raiz = rotacao_esquerda(raiz)
  pre = []
  pos = []

  pre_ordem(raiz, pre)
  pos_ordem(raiz, pos)
  
  print(f"Arvore {arvore_num}")

  print("pre: " + " ".join(map(str, pre)) + " ")
  print("pos: " + " ".join(map(str, pos)) + " ")
  print()
  arvore_num += 1