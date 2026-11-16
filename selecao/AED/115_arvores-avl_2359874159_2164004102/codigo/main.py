import sys

class No:

  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None
    self.alt = 1

def altura(no):
  if no is None:
    return 0
  return no.alt

def atualizar_altura(no):
  if no is None:
    return
  alt_esq = altura(no.esq)
  alt_dir = altura(no.dir)
  no.alt = 1 + max(alt_esq, alt_dir)
  
def inserir(raiz, valor):
  if raiz is None:
    return No(valor)
  if valor < raiz.valor:
    raiz.esq = inserir(raiz.esq, valor)
  else:
    raiz.dir = inserir(raiz.dir, valor)

  atualizar_altura(raiz)
  return raiz

def rotacaoLL(raiz):
  if raiz is None or raiz.esq is None:
    return raiz

  nova_raiz = raiz.esq
  raiz.esq = nova_raiz.dir
  nova_raiz.dir = raiz

  atualizar_altura(raiz)
  atualizar_altura(nova_raiz)
  
  return nova_raiz

def calcular_fb(no):
  if no is None:
    return 0
  return altura(no.dir) - altura(no.esq)

def pre_ordem(no, res):
  if no is None:
    return
  res.append(str(no.valor))
  pre_ordem(no.esq, res)
  pre_ordem(no.dir, res)

def pos_ordem(no, res):
  if no is None:
    return
  pos_ordem(no.esq, res)
  pos_ordem(no.dir, res)
  res.append(str(no.valor))


cont = 1

for linha in sys.stdin:
  entrada = eval(linha)
  if not entrada:
    break

  raiz = None
  for val in entrada:
    raiz = inserir(raiz, val)

  raiz = rotacaoLL(raiz)

  alt_final = altura(raiz)
  fb_final = calcular_fb(raiz)
  
  res_pre, res_pos = [], []

  pre_ordem(raiz, res_pre)
  pos_ordem(raiz, res_pos)

  print(f"Arvore {cont}")
  print(f"h: {alt_final}")
  print(f"fb: {fb_final}")
  print(f"pre: {' '.join(res_pre)}")
  print(f"pos: {' '.join(res_pos)}")
  print()

  cont += 1