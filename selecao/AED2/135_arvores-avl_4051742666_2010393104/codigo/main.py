def insere(arvore, valor):
  if arvore is None:
    arvore = cria_no(valor)
    
  if valor < arvore['valor']:
    arvore['esq'] = insere(arvore['esq'],valor)
  elif valor > arvore['valor']:
    arvore['dir'] = insere(arvore['dir'],valor)

  return arvore

def cria_no(valor):
    return {'valor': valor, 'esq': None, 'dir': None}

def pre_ordem(arvore):
    if arvore is not None:
      print(arvore['valor'], end=' ')
      pre_ordem(arvore['esq'])
      pre_ordem(arvore['dir'])

def pos_ordem(arvore):
    if arvore is not None:     
      pos_ordem(arvore['esq'])
      pos_ordem(arvore['dir'])
      print(arvore['valor'], end=' ')       
      

def rotacaoRR(arvore):
  if arvore is None:
    return arvore
  if arvore['dir'] is None:
    return arvore

  raiz_avl= arvore['dir']
  arvore['dir'] = raiz_avl['esq']
  raiz_avl['esq']= arvore
  return raiz_avl
  

i= 1
entrada= eval(input())

while entrada != []:
  arvore = None

  for valor in entrada:
    arvore = insere(arvore, valor)

  arvore = rotacaoRR(arvore)  
  print(f"Arvore {i}" )
  print(f"pre:", end = ' ')
  pre_ordem(arvore)
  print()
  print(f"pos:", end = ' ')
  pos_ordem(arvore)

  i+=1
  entrada= eval(input())
  
  