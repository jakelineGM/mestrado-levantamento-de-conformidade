#ctrl c e ctrl v do codigo da questao 03

def insere(arvore, valor):
  if arvore is None:
    return cria_no(valor)
  elif valor < arvore['valor']:
    arvore['esq'] = insere(arvore['esq'], valor)
  else:
    arvore['dir'] = insere(arvore['dir'], valor)
  return arvore

def cria_arvore():
  return None

def cria_no(valor):
  return {'valor': valor, 'esq': None, 'dir': None}

def pre_ordem(raiz):
  if raiz is not None:
    print(raiz['valor'], end=' ')
    pre_ordem(raiz['esq'])
    pre_ordem(raiz['dir'])

def pos_ordem(raiz):
  if raiz is not None:
    pos_ordem(raiz['esq'])
    pos_ordem(raiz['dir'])
    print(raiz['valor'], end=' ')

def rotacao(T):
  if T is None or T['dir'] is None:
    return T
  novaRaiz = T['dir']
  T['dir'] = novaRaiz['esq']
  novaRaiz['esq'] = T
  return novaRaiz

cont =  1
linha = input()

while linha.strip() != '[]':
  lista = eval(linha.strip())
  arvore = cria_arvore()

  for i in lista:
    arvore = insere(arvore, i)

  arvore = rotacao(arvore)
  print(f"Arvore {cont}")

  print("pre:", end=' ')
  pre_ordem(arvore)
  print()

  print("pos:", end=' ')
  pos_ordem(arvore)
  print()
  print()

  cont += 1
  linha = input()


  