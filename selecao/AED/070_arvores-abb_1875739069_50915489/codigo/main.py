import sys

def cria_nodo(valor):
  nodo = dict()

  nodo["valor"] = valor
  nodo["esq"] = None
  nodo["dir"] = None

  return nodo

def insere(raiz, valor):
  if raiz is None:
    return cria_nodo(valor)

  if valor < raiz["valor"]:
    raiz["esq"] = insere(raiz["esq"], valor)
  elif valor > raiz["valor"]:
    raiz["dir"] = insere(raiz["dir"], valor)

  return raiz

def pre_ordem(raiz, resultado):
  if raiz:
    resultado.append(str(raiz["valor"]))
    pre_ordem(raiz['esq'], resultado)
    pre_ordem(raiz['dir'], resultado)

def in_ordem(raiz, resultado):
  if raiz:
    in_ordem(raiz['esq'], resultado)
    resultado.append(str(raiz["valor"]))
    in_ordem(raiz['dir'], resultado)

def pos_ordem(raiz, resultado):
  if raiz:
    pos_ordem(raiz['esq'], resultado)
    pos_ordem(raiz['dir'], resultado)
    resultado.append(str(raiz["valor"]))

def simula():
  arvores = 1
  
  while True:
    entrada = eval(sys.stdin.readline())
    
    if not entrada:
      return 

    raiz = None
  
    for num in entrada:
      raiz = insere(raiz, num)
  
    print(f"Arvore {arvores}")

    res_pre = []
    pre_ordem(raiz, res_pre)
    str_res_pre = ' '.join(res_pre) 
    print(f'Pre-ordem: {str_res_pre}')

    res_in = []
    in_ordem(raiz, res_in)
    str_res_in = ' '.join(res_in)
    print(f'In-ordem: {str_res_in}')

    res_pos = []
    pos_ordem(raiz, res_pos)
    str_res_pos = ' '.join(res_pos)
    print(f'Pos-ordem: {str_res_pos}')

    print()

    arvores += 1

simula()