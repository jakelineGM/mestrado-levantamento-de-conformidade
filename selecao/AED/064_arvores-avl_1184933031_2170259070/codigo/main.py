def altura(no):
  if no is None:
    return 0
  return no['h']

def atualizar_altura(no):
  no['h'] = max(altura(no['esq']), altura(no['dir'])) + 1

def fator_balanceamento(no):
  return altura(no['dir']) - altura(no['esq'])

def rotacaoLL(T):
  nova_raiz = T['esq']
  sub_dir = nova_raiz['dir']

  nova_raiz['dir'] = T
  T['esq'] = sub_dir

  atualizar_altura(T)
  atualizar_altura(nova_raiz)

  return nova_raiz

def rotacaoRR(T):
  nova_raiz = T['dir']
  sub_esq = nova_raiz['esq']

  nova_raiz['esq'] = T
  T['dir'] = sub_esq

  atualizar_altura(T)
  atualizar_altura(nova_raiz)

  return nova_raiz

def inserir(T, chave):
  if T is None:
    return {'valor': chave, 'esq': None, 'dir': None, 'h': 1}
    
  if chave < T['valor']:
    T['esq'] = inserir(T['esq'], chave)
  
  else:
    T['dir'] = inserir(T['dir'], chave)

  atualizar_altura(T)
  fb = fator_balanceamento(T)

  if fb > 1:
    if fator_balanceamento(T['dir']) < 0:
      T['dir'] = rotacaoLL(T['dir'])
    T = rotacaoRR(T)
    
  elif fb < -1:
    if fator_balanceamento(T['esq']) > 0:
      T['esq'] = rotacaoRR(T['esq'])
    T = rotacaoLL(T)  

  return T

def pre_ordem(T, res):
  if T is not None:
    res.append(T['valor'])
    pre_ordem(T['esq'], res)
    pre_ordem(T['dir'], res)

def pos_ordem(T, res):
  if T is not None:
     pos_ordem(T['esq'], res)
     pos_ordem(T['dir'], res)
     res.append(T['valor'])

num_arvore = 1

while True:
  try:
    linha = input().strip()
  except EOFError:
    break

  if linha == "":
      continue

  valores = eval(linha)

  if valores == []:
    break

  raiz = None
  for v in valores:
      raiz = inserir(raiz, v)

  pre = []
  pos = []
  pre_ordem(raiz, pre)
  pos_ordem(raiz, pos)

  print("Arvore", num_arvore)
  print("pre:", " ".join(str(x) for x in pre))
  print("pos:", " ".join(str(x) for x in pos))
  print()

  num_arvore += 1
