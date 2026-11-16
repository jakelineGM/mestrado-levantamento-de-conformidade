def cria_arvore_vazia():
  return None

def cria_nodo(valor):
  return {'valor': valor, 'esq': None, 'dir': None, 'h': 1}

def obter_altura(nodo):
  if nodo is None:
    return 0
  else:
    return nodo['h']

def rotacaoRR(T):
  nova_raiz = T['dir']
  T['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = T

  T['h'] = 1 + max(obter_altura(T['esq']), obter_altura(T['dir']))
  nova_raiz['h'] = 1 + max(obter_altura(nova_raiz['esq']), obter_altura(nova_raiz['dir']))
  
  return nova_raiz

def rotacaoLL(T):
  nova_raiz = T['esq']
  T['esq'] = nova_raiz['dir']
  nova_raiz['dir'] = T

  T['h'] = 1 + max(obter_altura(T['esq']), obter_altura(T['dir']))
  nova_raiz['h'] = 1 + max(obter_altura(nova_raiz['esq']), obter_altura(nova_raiz['dir']))

  return nova_raiz

def rotacaoLR(T):
  T['esq'] = rotacaoRR(T['esq'])
  return rotacaoLL(T)

def rotacaoRL(T):
  T['dir'] = rotacaoLL(T['dir'])
  return rotacaoRR(T)

def pre_ordem(T):
  if T is not None:
    print(T['valor'], end=' ')
    pre_ordem(T['esq'])
    pre_ordem(T['dir'])

def pos_ordem(T):
  if T is not None:
    pos_ordem(T['esq'])
    pos_ordem(T['dir'])
    print(T['valor'], end=' ')

def insere(raiz, chave):
  if raiz is None:
    return cria_nodo(chave)
  elif chave < raiz['valor']:
    raiz['esq'] = insere(raiz['esq'], chave)
  else:
    raiz['dir'] = insere(raiz['dir'], chave)

  raiz['h'] = 1 + max(obter_altura(raiz['esq']), obter_altura(raiz['dir']))

  fb = obter_altura(raiz['dir']) - obter_altura(raiz['esq'])
  
  if fb > 1:
    filho_direito = raiz['dir']
    fb_fd = obter_altura(filho_direito['dir']) - obter_altura(filho_direito['esq'])
    if fb_fd < 0:
      raiz = rotacaoRL(raiz)
    else:
      raiz = rotacaoRR(raiz)
  elif fb < -1:
    filho_esquerdo = raiz['esq']
    fb_fe = obter_altura(filho_esquerdo['dir']) - obter_altura(filho_esquerdo['esq'])
    if fb_fe > 0:
      raiz = rotacaoLR(raiz)
    else:
      raiz = rotacaoLL(raiz)

  return raiz

lista = eval(input())
k = 0

while len(lista) != 0:
  k += 1

  arvore = cria_arvore_vazia()

  for i in lista:
    arvore = insere(arvore, i)

  print(f"Arvore {k}")
  print("pre: ", end=' ')
  pre_ordem(arvore)
  print()
  print("pos: ", end=' ')
  pos_ordem(arvore)
  print()

  lista = eval(input())




  