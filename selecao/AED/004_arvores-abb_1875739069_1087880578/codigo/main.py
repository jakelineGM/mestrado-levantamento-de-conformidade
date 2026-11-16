class No:
  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None

def inserir(raiz, valor):
  if raiz is None:
    return No(valor)
  if valor < raiz.valor:
    raiz.esq = inserir(raiz.esq, valor)
  elif valor > raiz.valor:
    raiz.dir = inserir(raiz.dir, valor)
  return raiz

def pre_ordem(no, resultado):
  if no is not None:
    resultado.append(str(no.valor))
    pre_ordem(no.esq, resultado)
    pre_ordem(no.dir, resultado)

def in_ordem(no, resultado):
  if no is not None:
    in_ordem(no.esq, resultado)
    resultado.append(str(no.valor))
    in_ordem(no.dir, resultado)
    
def pos_ordem(no, resultado):
  if no is not None:
    pos_ordem(no.esq, resultado)
    pos_ordem(no.dir, resultado)
    resultado.append(str(no.valor))

num_arvore = 1
primeira = True

while True:
  linha = input().strip()

  if linha == "[]":
    break 

  elementos = eval(linha)

  raiz = None
  for x in elementos:
    raiz = inserir(raiz, x)

  if not primeira:
    print()
  primeira = False

  print(f"Arvore {num_arvore}")

  pre = []
  ino = []
  pos = []

  pre_ordem(raiz, pre)
  in_ordem(raiz, ino)
  pos_ordem(raiz, pos)

  print("Pre-ordem: " + " ".join(pre) + " ")
  print("In-ordem: " + " ".join(ino) + " ")
  print("Pos-ordem: " + " ".join(pos) + " ")

  num_arvore += 1