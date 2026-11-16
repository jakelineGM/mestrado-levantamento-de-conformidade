def cria_arvore():
  return None
  
def cria_no(k):
  no = dict()
  no['valor'] = k
  no['esq'] = None
  no['dir'] = None
  return no

def inserir(arv, k):
  if arv is None:
    arv = cria_no(k)
  elif arv['valor'] >= k:
    arv['esq'] = inserir(arv['esq'], k)
  else:
    arv['dir'] = inserir(arv['dir'], k)

  return arv

def pre_ordem(arv):
  if arv:
    print(arv['valor'], end=' ')
    pre_ordem(arv['esq'])
    pre_ordem(arv['dir'])

def in_ordem(arv):
  if arv:
    in_ordem(arv['esq'])
    print(arv['valor'], end=' ')
    in_ordem(arv['dir'])

def pos_ordem(arv):
  if arv:
    pos_ordem(arv['esq'])
    pos_ordem(arv['dir'])
    print(arv['valor'], end=' ')

cont = 1
while True:
  arv_l = eval(input())
  if arv_l == []:
    break

  arv = cria_arvore()
  for elem in arv_l:
    arv = inserir(arv, elem)
  
  
  print('Arvore', cont)
  print("Pre-ordem:")
  pre_ordem(arv)
  print("")
  print("In-ordem:") 
  in_ordem(arv)
  print("")
  print("Pos-ordem:")
  pos_ordem(arv)
  print("")
  print("")
  cont += 1
