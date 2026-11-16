def cria_nodo(valor):
  return {'valor': valor, 'esq': None, 'dir': None, 'h': 1}

def cria_arvore_vazia():
  return None

def insere(raiz, chave):
  if raiz is None:
    return cria_nodo(chave)
  if chave < raiz['valor']:
    raiz['esq'] = insere(raiz['esq'], chave)
  else:
    raiz['dir'] = insere(raiz['dir'], chave)

  raiz['h'] = 1 + max(obter_altura(raiz['esq']), obter_altura(raiz['dir']))
  
  return raiz

def obter_altura(nodo):
  if nodo is None:
    return 0
  else:
    return nodo['h']

def rotacaoLL(T):
  nova_raiz = T['esq']
  T['esq'] = nova_raiz['dir']
  nova_raiz['dir'] = T

  T['h'] = 1 + max(obter_altura(T['esq']), obter_altura(T['dir']))
  nova_raiz['h'] = 1 + max(obter_altura(nova_raiz['esq']), obter_altura(nova_raiz['dir']))

  return nova_raiz

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

lista = eval(input())
k = 1

while len(lista) != 0:
  arvore = cria_arvore_vazia()

  for i in lista:
    arvore = insere(arvore, i)

  arvore = rotacaoLL(arvore)
  altura_raiz = obter_altura(arvore)

  fb = abs(obter_altura(arvore['esq']) - obter_altura(arvore['dir']))

  print(f"Arvore {k}")
  print(f"h: {altura_raiz}")
  print(f"fb: {fb}")
  print("pre: ", end='')
  pre_ordem(arvore)
  print()
  print("pos: ", end='')
  pos_ordem(arvore)
  print()

  lista = eval(input())
  k += 1

