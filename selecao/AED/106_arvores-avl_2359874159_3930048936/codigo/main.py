def cria_node(valor):
  node = dict()

  node['valor'] = valor
  node['esq'] = None
  node['dir'] = None
  node['h'] = 1

  return node

def altura(arvore):
  if arvore is None:
    return 0

  return arvore['h']

def calcular_fb(arvore):
  if arvore is None:
    return 0

  fb = altura(arvore['dir']) - altura(arvore['esq'])
  
  return fb

def calcular_h(arvore):
  arvore['h'] = max(altura(arvore['esq']), altura(arvore['dir'])) + 1
  
  return arvore['h']

def inserir(arvore, chave):
  if arvore is None:
    return cria_node(chave)
  elif arvore['valor'] >= chave:
    arvore['esq'] = inserir(arvore['esq'], chave) 
  else:
    arvore['dir'] = inserir(arvore['dir'], chave)

  calcular_h(arvore)
  
  return arvore

def rotacaoLL(T):
  filho_esquerdo = T['esq']
  filho_direito_do_filho_esquerdo = filho_esquerdo['dir']
  filho_esquerdo['dir'] = T
  T['esq'] = filho_direito_do_filho_esquerdo

  calcular_h(T)
  calcular_h(filho_esquerdo)
  
  return filho_esquerdo

def imprimir_preOrdem(arvore):
  if arvore is not None:
    print(arvore['valor'], end=" ")
    imprimir_preOrdem(arvore['esq'])
    imprimir_preOrdem(arvore['dir'])

def imprimir_posOrdem(arvore):
  if arvore is not None:
    imprimir_posOrdem(arvore['esq'])
    imprimir_posOrdem(arvore['dir'])
    print(arvore['valor'], end=" ")

chaves = eval(input())
cont = 0
while chaves != []:
  cont += 1
  # Insere a primeira chave na raiz da arvore
  arvore = cria_node(chaves[0])
  # Insere o restante das chaves a partir da segunda
  for chave in chaves[1:]:
    arvore = inserir(arvore, chave)
  arvore = rotacaoLL(arvore)
  print("Arvore %d" % cont)
  print("h: %d" % arvore['h'])
  print("fb: %d" % calcular_fb(arvore))
  print("pre:", end=" ")
  imprimir_preOrdem(arvore)
  print("\npos:", end=" ")
  imprimir_posOrdem(arvore)
  print()
  chaves = eval(input())