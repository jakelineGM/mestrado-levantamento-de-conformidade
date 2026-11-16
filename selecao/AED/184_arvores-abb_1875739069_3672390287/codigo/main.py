import sys

sys.setrecursionlimit(100000)

class No:
  def __init__(self, v):
    self.valor = v
    self.esq = None
    self.dir = None

def inserir(no, v):
  if not no: 
    return No(v)
  if v < no.valor: 
      no.esq = inserir(no.esq, v)
  else:
      no.dir = inserir(no.dir, v)
  return no

def pre_ordem(no):
  if not no:
    return
  yield no.valor
  yield from pre_ordem(no.esq)
  yield from pre_ordem(no.dir)

def in_ordem(no):
  if not no:
    return
  yield from in_ordem(no.esq)
  yield no.valor
  yield from in_ordem(no.dir)

def pos_ordem(no):
  if not no:
    return
  yield from pos_ordem(no.esq)
  yield from pos_ordem(no.dir)
  yield no.valor

def main():
  contador = 1
  while True:
    try:
      linha = input()
      if not linha.strip():
        continue
      lista = eval(linha)
      if not lista:
        break
      raiz = None
      for v in lista:
        raiz = inserir(raiz, v)

      print(f"Arvore {contador}")
      print(f"Pre-ordem:", *pre_ordem(raiz))
      print(f"In-ordem:", *in_ordem(raiz))
      print(f"Pos-ordem:", *pos_ordem(raiz))
      print()
      contador += 1

    except EOFError:
      break

if __name__ == "__main__":
  main()
    
    