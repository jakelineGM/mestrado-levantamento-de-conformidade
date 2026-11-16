def pre_ordem(arvore):
  if arvore is not None:
    print(arvore['valor'], end=" ")
    pre_ordem(arvore['esq'])
    pre_ordem(arvore['dir'])

def in_ordem(arvore):
  if arvore is not None:   
    in_ordem(arvore['esq'])
    print(arvore['valor'], end=" ")
    in_ordem(arvore['dir'])

def pos_ordem(arvore):
  if arvore is not None:   
    pos_ordem(arvore['esq'])
    pos_ordem(arvore['dir'])
    print(arvore['valor'], end=" ")
    
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


# Lê o primeiro caso de teste
caso = eval(input())
conta_casos = 0

# Itera até o último caso
while caso != []:
  conta_casos += 1
  
  arvore = cria_arvore()
  for nodo in caso:
    arvore = insere(arvore, nodo)
    
  print("Arvore", conta_casos)
  
  print("Pre-ordem:", end=" ")
  pre_ordem(arvore)
  print()

  print("In-ordem:", end=" ")
  in_ordem(arvore)
  print()

  print("Pos-ordem:", end=" ")
  pos_ordem(arvore)
  print()

  
  # Lê o próximo caso de teste
  caso = eval(input())

