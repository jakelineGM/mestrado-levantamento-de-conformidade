import sys

class No:
  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None
    self.altura = 1

def obter_altura(no):
  if no is None:
    return 0
  return no.altura

def atualiza_altura(no):
  no.altura = 1 +max(obter_altura(no.esq), obter_altura(no.dir))

def fator_balanceamento(no):
  return obter_altura(no.esq) - obter_altura(no.dir)

def rotacao_dir(y):
  x = y.esq
  t2 = x.dir

  x.dir = y
  y.esq = t2

  atualiza_altura(y)
  atualiza_altura(x)
  return x

def rotacao_esq(x):
  y = x.dir
  t2 = y.esq

  y.esq = x
  x.dir = t2

  atualiza_altura(x)
  atualiza_altura(y)
  return y

def inserir(no, valor):
  if no is None:
    return No(valor)
  if valor < no.valor:
    no.esq = inserir(no.esq, valor)
  elif valor > no.valor:
    no.dir = inserir(no.dir, valor)
  else:
    return no

  atualiza_altura(no)
  fb = fator_balanceamento(no)

  if fb > 1 and valor < no.esq.valor:
    return rotacao_dir(no)
  if fb > 1 and valor > no.esq.valor:
    no.esq = rotacao_esq(no.esq)
    return rotacao_dir(no)
    
  if fb < -1 and valor > no.dir.valor:
    return rotacao_esq(no)
  if fb < -1 and valor < no.dir.valor:
    no.dir = rotacao_dir(no.dir)
    return rotacao_esq(no)
  return no

def percurso_pre(no, resultado):
  if no is not None:
    resultado.append(str(no.valor))
    percurso_pre(no.esq, resultado)
    percurso_pre(no.dir, resultado)

def percurso_pos(no, resultado):
  if no is not None:
    percurso_pos(no.esq, resultado)
    percurso_pos(no.dir, resultado)
    resultado.append(str(no.valor))

def interpretar_lista(texto):
  texto = texto.strip()
  conteudo = texto[1:-1].strip()
  if conteudo == "":
    return []
  partes = conteudo.split(',')
  valores = []
  for p in partes:
    p = p.strip()
    if p != "":
      valores.append(int(p))
  return valores

def main():
  numero_arvore = 1
  for linha in sys.stdin:
    linha = linha.strip()
    if linha == "":
      continue
    if linha == "[]":
      break
    valores = interpretar_lista(linha)
    raiz = None
    for v in valores:
      raiz = inserir(raiz, v)
    pre = []
    pos = []
    percurso_pre(raiz, pre)
    percurso_pos(raiz, pos)

    print("Arvore {}".format(numero_arvore))
    print("pre: ", " ".join(pre))
    print("pos: ", " ".join(pos))
    print()

    numero_arvore += 1
if __name__ == "__main__":
  main()
