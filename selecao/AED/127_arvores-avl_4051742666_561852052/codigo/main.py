class No:
  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None

def inserir(raiz, valor):
  if raiz is None: return No(valor)
  if valor < raiz.valor: raiz.esq = inserir(raiz.esq, valor)
  else: raiz.dir = inserir(raiz.dir, valor)
  return raiz

def rotacaoRR(raiz):
  if not raiz or not raiz.dir: return raiz

  nova_raiz = raiz.dir
  raiz.dir = nova_raiz.esq
  nova_raiz.esq = raiz

  return nova_raiz

def pre_ordem(raiz):
  if raiz:
    print(f"{raiz.valor}", end = " ")
    pre_ordem(raiz.esq)
    pre_ordem(raiz.dir)

def pos_ordem(raiz):
  if raiz:
    pos_ordem(raiz.esq)
    pos_ordem(raiz.dir)
    print(f"{raiz.valor}", end = ' ')


def main():
  contador = 1
  while True:
    try:
      entrada = input()
      if not entrada: break 
      lista = eval(entrada)
      if not lista: break 

      raiz = None

      for val in lista:
        raiz = inserir(raiz, val)

      raiz = rotacaoRR(raiz)

      print(f"Arvore {contador}")
      print("pre:", end=" ")
      pre_ordem(raiz)

      print("\npos:", end = " ")
      pos_ordem(raiz)
      print("\n")

      contador += 1

    except: break


if __name__ == "__main__":
  main()