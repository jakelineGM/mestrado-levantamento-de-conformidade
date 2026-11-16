def cria_novo(valor):
  novo_no = dict()
  novo_no['valor'] = valor
  novo_no['esq'] = None
  novo_no['dir'] = None
  novo_no['h'] = 1
  return novo_no

def inserir(T, valor):
  if T is None:
    T = cria_novo(valor)
  elif T['valor'] >= valor:
    T['esq'] = inserir(T['esq'], valor)
  else:
    T['dir'] = inserir(T['dir'], valor)

  hT = atualiza_altura(T)  

  hEsq = 0
  if T['esq'] is not None:
    hEsq = T['esq']['h']

  hDir = 0
  if T['dir'] is not None:
    hDir = T['dir']['h']
  
  fb = calcula_fb(T)

  if fb > 1:    
    if calcula_fb(T['dir']) < 0:
      print("Rotacao dupla (RL)")
      T['dir'] = rotacaoLL(T['dir'])    
    T = rotacaoRR(T)
  elif fb < -1:
    if calcula_fb(T['esq']) > 0:
      T['esq'] = rotacaoRR(T['esq'])
    T = rotacaoLL(T)
   
  
  hT = atualiza_altura(T)
  
  return T

def atualiza_altura(T):
  if T is None:
    return 0
  else:
    hEsq = atualiza_altura(T['esq'])
    hDir = atualiza_altura(T['dir'])
    if hEsq >= hDir:
      T['h'] = hEsq + 1
    else:
      T['h'] = hDir + 1    
    return T['h']

def calcula_fb(T):
  hEsq = 0
  if T['esq'] is not None:    
    hEsq = T['esq']['h']
    
  hDir = 0
  if T['dir'] is not None:
    hDir = T['dir']['h']

  return hDir - hEsq

def rotacaoRR(T):
  if T is not None:
    print(f"Rotacao RR com {T['valor']}")
    nova_raiz = T['dir']
    T['dir'] = nova_raiz['esq']
    nova_raiz['esq'] = T
    T = nova_raiz
    return T

def rotacaoLL(T):
  if T is not None:
    print(f"Rotacao LL com {T['valor']}")
    nova_raiz = T['esq']
    T['esq'] = nova_raiz['dir']
    nova_raiz['dir'] = T
    T = nova_raiz
    return T

def imprimir_pre_ordem(T):
  if T is not None:
    print(T['valor'], end=' ')
    imprimir_pre_ordem(T['esq'])
    imprimir_pre_ordem(T['dir'])

def imprimir_pos_ordem(T):
  if T is not None:
    imprimir_pos_ordem(T['esq'])
    imprimir_pos_ordem(T['dir'])
    print(T['valor'], end=' ')


arvores = []
entrada = eval(input())
while entrada != []:
  T = None
  for i in range(len(entrada)):
    T = inserir(T, entrada[i])    
  arvores += [T]
  entrada = eval(input())

for i in range(len(arvores)):
  T = arvores[i]
  print(f"Arvore {i+1}")
  print("pre: ", end='')
  imprimir_pre_ordem(T)
  print()
  print("pos: ", end='')
  imprimir_pos_ordem(T)
  print("\n")