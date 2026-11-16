def pre_ordem(arvore):
    if arvore is not None:
      print(arvore['valor'], end=' ')
      pre_ordem(arvore['esq'])
      pre_ordem(arvore['dir'])

def insere(arvore, valor):
  if arvore is None:
    arvore = cria_no(valor)
    
  if valor < arvore['valor']:
    arvore['esq'] = insere(arvore['esq'],valor)
  elif valor > arvore['valor']:
    arvore['dir'] = insere(arvore['dir'],valor)

  return arvore

def cria_arvore():
   return None


def cria_no(valor):
    return {'valor': valor, 'esq': None, 'dir': None}

def sucessor(arvore):
  if arvore['esq'] is not None:
    return sucessor(arvore['esq'])
  else:
    return arvore['valor']  

def remover(arvore, valor):
  if arvore is None:
    return None
  if arvore['valor'] > valor:
    arvore['esq'] = remover(arvore['esq'], valor)
  elif arvore['valor'] < valor:
    arvore['dir'] = remover(arvore['dir'], valor)
  else:
    if arvore['esq'] is None:
      return arvore['dir']
    elif arvore['dir'] is None :
      return arvore['esq']
    else:
      suc = sucessor(arvore['dir'])
      arvore['valor'] = suc
      arvore['dir'] = remover(arvore['dir'], suc)
      
  
  return arvore


lis = eval(input())
chaves = eval(input())
arvore = cria_arvore()
   
for no in lis:
  arvore = insere(arvore, no)
  
print(f'Arvore inicial:', end = ' ')
pre_ordem(arvore)
print()

for chave in chaves:
  arvore = remover(arvore, chave)

  print(f'Depois de remover {chave}: ', end =' ')

  if arvore is None:
    print('vazia!')
  else:
    pre_ordem(arvore)
    print()
  
