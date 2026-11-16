def insere(arvore, valor):
  if arvore is None:
    arvore = cria_no(valor)
  elif arvore['valor'] > valor:
    arvore['esq'] = insere(arvore['esq'], valor)
  else:
    arvore['dir'] = insere(arvore['dir'], valor)
  return arvore  

def cria_arvore():
  """Cria uma árvore vazia.
  """
  return None


def cria_no(valor):
  """Cria um novo nó que não contém filhos e possui o valor
  especificado no argumento como chave."""
  return {'valor': valor, 'esq': None, 'dir': None}

def pre_ordem(arvore):
  
  if arvore is not None:
    print(arvore['valor'], end = ' ')
    pre_ordem(arvore['esq'])
    pre_ordem(arvore['dir'])

def pos_ordem(arvore):
  
  if arvore is not None:
    pos_ordem(arvore['esq'])
    pos_ordem(arvore['dir'])
    print(arvore['valor'], end = ' ')

def rotacaoRR(raiz):
  dir_antiga = raiz['dir']
  raiz['dir'] = dir_antiga['esq']
  dir_antiga['esq'] = raiz
  return dir_antiga

caso = eval(input())
quantidade = 0

while caso != []:
  quantidade += 1
  arvore = cria_arvore()

  for i in range(len(caso)):
    arvore = insere(arvore, caso[i])

  arvore = rotacaoRR(arvore)
  print(f"Arvore {quantidade}")
  print("pre: ", end = '')
  pre_ordem(arvore)
  print()
  print("pos: ", end = '')
  pos_ordem(arvore)
  print()

  caso = eval(input())


  
    