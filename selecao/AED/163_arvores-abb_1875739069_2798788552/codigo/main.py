def cria_no(valor):
  novo_no = dict()
  novo_no['valor'] = valor
  novo_no['esq'] = None
  novo_no['dir'] = None
  return novo_no

def inserir(T, valor):
  if T is None:
    T = cria_no(valor)
  if valor < T['valor']:
    T['esq'] = inserir(T['esq'], valor)
  elif valor > T['valor']:
    T['dir'] = inserir(T['dir'], valor)
  return T

def imprimir_pre_ordem(T):
  if T is not None:    
    print(T['valor'], end=' ')
    imprimir_pre_ordem(T['esq'])
    imprimir_pre_ordem(T['dir'])


def imprimir_in_ordem(T):
  if T is not None:    
    imprimir_in_ordem(T['esq'])
    print(T['valor'], end=' ')
    imprimir_in_ordem(T['dir'])


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
  print("Pre-ordem: ", end='')
  imprimir_pre_ordem(T)
  print()
  print("In-ordem: ", end='')
  imprimir_in_ordem(T)
  print()
  print("Pos-ordem: ", end='')
  imprimir_pos_ordem(T)
  print("\n")
  