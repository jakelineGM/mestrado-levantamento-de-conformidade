class No:
  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None
    self.h = 1

def altura(no):
  return no.h if no else 0

def atualizar_altura(no):
  if no:
    no.h = 1 + max(altura(no.esq), altura(no.dir))

def fator_balanceamento(no):
  return altura(no.dir) - altura(no.esq) if no else 0

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

def pre_ordem(raiz, resultado):
  if raiz is not None:
    resultado.append(str(raiz.valor))
    pre_ordem(raiz.esq, resultado)
    pre_ordem(raiz.dir, resultado)

def in_ordem(raiz, resultado):
  if raiz is not None:
    in_ordem(raiz.esq, resultado)
    resultado.append(str(raiz.valor))
    in_ordem(raiz.dir, resultado)

def pos_ordem(raiz, resultado):
  if raiz is not None:
    pos_ordem(raiz.esq, resultado)
    pos_ordem(raiz.dir, resultado)
    resultado.append(str(raiz.valor))

def processa_arvores():
  entradas = []
  while True:
    entrada = input().strip()
    if entrada == "[]":
      break 
    entradas.append(eval(entrada))

  contador = 1
  print()
  for elementos in entradas:
    raiz = None
    for elemento in elementos:
      raiz = inserir(raiz, elemento)
    raiz = rotacaoLL(raiz)
    if contador>1:
      print()
    print(f"Arvore {contador}")
    print(f"h: {altura(raiz)}")
    print(f"fb: {fator_balanceamento(raiz)}")
    resultado_pre = []
    pre_ordem(raiz, resultado_pre)
    print("pre:", " ".join(resultado_pre))
    resultado_pos = []
    pos_ordem(raiz, resultado_pos)
    print("pos:", " ".join(resultado_pos))
    contador+=1

if __name__ == "__main__":
  processa_arvores()