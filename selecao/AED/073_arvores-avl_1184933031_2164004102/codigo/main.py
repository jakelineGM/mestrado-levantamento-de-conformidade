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

def calcular_fb(no):
  if no is None:
    return 0
  return altura(no.dir) - altura(no.esq)

def rotacao_direita(no):
  esq = no.esq
  esq_dir_no = esq.dir

  esq.dir = no
  no.esq = esq_dir_no

  atualizar_altura(no)
  atualizar_altura(esq)
  
  return esq

def rotacao_esquerda(no):
  dir = no.dir
  dir_esq_no = dir.esq

  dir.esq = no
  no.dir = dir_esq_no

  atualizar_altura(no)
  atualizar_altura(dir)
  
  return dir
  
def inserir(no, valor):
  if no is None:
    return No(valor)
  if valor < no.valor:
    no.esq = inserir(no.esq, valor)
  else:
    no.dir = inserir(no.dir, valor)

  atualizar_altura(no)
  fb = calcular_fb(no)

  if fb > 1:
    return rotacao_esquerda(no)
  if fb < -1:
    return rotacao_direita(no)
  
  return no

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

  res_pre, res_pos = [], []

  pre_ordem(raiz, res_pre)
  pos_ordem(raiz, res_pos)

  print(f"Arvore {cont}")
  print(f"pre: {' '.join(res_pre)}")
  print(f"pos: {' '.join(res_pos)}")
  print()

  cont += 1