def criar_vertice(valor):
  vertice = {}
  vertice['valor'] = valor
  vertice['esq'] = None
  vertice['dir'] = None
  vertice['h'] = 1
  return vertice

def calcular_altura(no):
  if no is None:
    return 0
  return no['h']

def atualizar_altura(no):
  if no is not None:
    no['h'] = 1 + max(calcular_altura(no['esq']), calcular_altura(no['dir']))

def calcular_fator_balanceamento(no):
  if no is None:
    return 0
  return calcular_altura(no['dir']) - calcular_altura(no['esq'])

def balancear_no(no):
  atualizar_altura(no)

  fator_balanceamento = calcular_fator_balanceamento(no)

  #rotacao simples à direita
  if fator_balanceamento > 1 and calcular_fator_balanceamento(no['dir']) >= 0:
    return rotacao_esquerda(no)

  if fator_balanceamento < -1 and calcular_fator_balanceamento(no['esq']) <= 0:
    return rotacao_direita(no)

  return no

def inserir(no, valor):
  if no == None:
    return criar_vertice(valor)
  if valor > no['valor']:
    no['dir'] = inserir(no['dir'], valor)
  else:
    no['esq'] = inserir(no['esq'], valor)

  return balancear_no(no)

def preordem(raiz):
  if raiz:
    print(raiz['valor'], end=' ')
    preordem(raiz['esq'])
    preordem(raiz['dir'])

def inordem(raiz):
  if raiz:
    inordem(raiz['esq'])
    print(raiz['valor'], end=' ')
    inordem(raiz['dir'])

def posordem(raiz):
  if raiz:
    posordem(raiz['esq'])
    posordem(raiz['dir'])
    print(raiz['valor'], end=' ')

def rotacao_esquerda(x):
  y = x['dir']
  T = y['esq']

  y['esq'] = x
  x['dir'] = T

  atualizar_altura(x)
  atualizar_altura(y)

  return y

def rotacao_direita(y):
  x = y['esq']
  T = x['dir']

  x['dir'] = y
  y['esq'] = T

  atualizar_altura(y)
  atualizar_altura(x)

  return x
  
arvore = eval(input())
i = 0
while arvore:
  raiz = None
  i += 1
  for v in arvore:
    raiz = inserir(raiz, int(v))
  
  print("Arvore", i)  
  print("pre:", end=' ')
  preordem(raiz)  
  print("\npos:", end=' ')
  posordem(raiz)
  print()
  
  arvore = eval(input())