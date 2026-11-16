def nova_arvore(valor):
  nova = {}
  nova['valor'] = valor
  nova['h'] = 1
  nova['esq'] = None
  nova['dir'] = None
  return nova
  
def update_h(arvore):
  if arvore['esq'] is None:
    h_esq = 0
  else:
    update_h(arvore['esq'])
    h_esq = arvore['esq']['h']
  if arvore['dir'] is None:
    h_dir = 0
  else:
    update_h(arvore['dir'])
    h_dir = arvore['dir']['h']
  arvore['h'] = max(h_esq, h_dir) + 1

def fator(arvore):
  h_dir = 0
  h_esq = 0
  if arvore['esq'] is not None:
    h_esq = arvore['esq']['h']
  if arvore['dir'] is not None:
    h_dir = arvore['dir']['h']
  return h_dir - h_esq

def RR(arvore):
  temp = arvore
  nova_raiz = arvore['dir']
  temp['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = temp
  update_h(nova_raiz)
  return nova_raiz
  
def LL(arvore):
  temp = arvore
  nova_raiz = arvore['esq']
  temp['esq'] = nova_raiz['dir']
  nova_raiz['dir'] = temp
  update_h(nova_raiz)
  return nova_raiz

  
def insere(arvore, valor):
  if valor <= arvore['valor'] and arvore['esq'] is None:
    arvore['esq'] = nova_arvore(valor)
  elif valor <= arvore['valor']:
    arvore['h'] +=1
    arvore['esq'] = insere(arvore['esq'], valor)
  elif valor > arvore['valor'] and arvore['dir'] is None:
    arvore['dir'] = nova_arvore(valor)
  elif valor > arvore['valor']:
    arvore['h'] +=1
    arvore['dir'] = insere(arvore['dir'], valor)
  update_h(arvore)
  if fator(arvore) < -1 and fator(arvore['esq']) > 0:
    arvore['esq'] = RR(arvore['esq'])
    arvore = LL(arvore)
  elif fator(arvore) > 1 and fator(arvore['dir']) < 0:
    arvore['dir'] = LL(arvore['dir'])
    arvore = RR(arvore)
  elif fator(arvore) < -1:
    arvore = LL(arvore)
  elif fator(arvore) > 1:
    arvore = RR(arvore)
  return arvore
  
def pre_ordem(arvore, lista):
  if arvore is not None:
    lista.append(arvore['valor'])
    pre_ordem(arvore['esq'], lista)
    pre_ordem(arvore['dir'], lista)
def pos_ordem(arvore, lista):
  if arvore is not None:
    pos_ordem(arvore['esq'], lista)
    pos_ordem(arvore['dir'], lista)
    lista.append(arvore['valor'])

  

count = 0
arvores = eval(input())
while arvores != []:
  count +=1
  print("Arvore", count)
  arvore = nova_arvore(arvores.pop(0))
  for e in arvores:
    arvore = insere(arvore, e)
  lista = []
  pre_ordem(arvore, lista)
  print("pre:", *lista)
  lista = []
  pos_ordem(arvore, lista)
  print("pos:", *lista)
  print()
  arvores = eval(input())