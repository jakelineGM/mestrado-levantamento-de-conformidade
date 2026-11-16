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
      

def rotacaoLL(arvore):
  if arvore is None:
    return arvore
  if arvore['esq'] is None:
    return arvore

  raiz_avl= arvore['esq']
  arvore['esq'] = raiz_avl['dir']
  raiz_avl['dir']= arvore
  return raiz_avl

def altura(arvore):
  if arvore is None:
    return 0
    
  if altura(arvore['esq']) > altura(arvore['dir']):
    return 1+ altura(arvore['esq'])
  else:
    return 1+ altura(arvore['dir'])
  

i= 1
entrada= eval(input())

while entrada != []:
  arvore = None

  for valor in entrada:
    arvore = insere(arvore, valor)

  
  arvore = rotacaoLL(arvore)  
  h = altura(arvore)  
  fb = altura(arvore['dir']) - altura(arvore['esq'])
  
  print(f"Arvore {i}" )
  print(f"h: {h}" )
  print(f"fb: {fb}" )


  
  print(f"pre:", end = ' ')
  pre_ordem(arvore)
  print()
  print(f"pos:", end = ' ')
  pos_ordem(arvore)

  i+=1
  entrada= eval(input())
  
  