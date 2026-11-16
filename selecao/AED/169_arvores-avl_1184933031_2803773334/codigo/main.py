import numpy as np

def altura(no):
  return no['h'] if no else 0

def fator_balanceamento(no):
  if not no:
    return 0
  return np.abs(altura(no['esq']) - altura(no['dir']))

def atualizar_altura(no):
  if no:
    no['h'] = 1 + max(altura(no['esq']), altura(no['dir'] ))

def inserir_avl(no, valor):
  if not no:
    #print(f"Criando no com valor {valor}")
    return {'valor':valor, 'esq':None, 'dir':None, 'h':1}
    
  if valor < no['valor']:
    #print(f"Inserindo {valor} a esquerda de {no['valor']}")
    no['esq'] = inserir_avl(no['esq'], valor)
  else:
    #print(f"Inserindo {valor} a direita de {no['valor']}")
    no['dir'] = inserir_avl(no['dir'], valor)

  atualizar_altura(no)

  fb = fator_balanceamento(no)
  #print(f"No {no['valor']} tem fator de balanceamento {fb}")
  
  if fb > 1:
    if no['esq'] and valor < no['valor']:
      return rotacaoLL(no)
    if no['dir'] and valor > no['valor']:
      return rotacaoRR(no)

  return no

def preordem(arvore, resultado):
  if arvore:
    resultado.append(arvore['valor'])
    preordem(arvore['esq'], resultado)
    preordem(arvore['dir'], resultado)

def posordem(arvore, resultado):
  if arvore:
    posordem(arvore['esq'], resultado)
    posordem(arvore['dir'], resultado)
    resultado.append(arvore['valor'])

def rotacaoLL(arvore):
  nova_raiz = arvore['esq']
  arvore['esq'] = nova_raiz['dir']
  nova_raiz['dir'] = arvore
  atualizar_altura(arvore)
  atualizar_altura(nova_raiz)
  return nova_raiz


def rotacaoRR(arvore):
  nova_raiz = arvore['dir']
  arvore['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = arvore
  atualizar_altura(arvore)
  atualizar_altura(nova_raiz)
  return nova_raiz

n_arvore = 1
while True:
  linha = input().strip()
  if linha == "[]":
    break
  elementos = eval(linha)
  if not elementos:
    continue 

  arvore = None
  for elemento in elementos:
    arvore = inserir_avl(arvore, elemento)
  
  pre = []
  pos = []
  
  preordem(arvore, pre)
  posordem(arvore, pos)
  
  print(f"Arvore {n_arvore}")
  print("pre:", " ".join(map(str, pre)))
  print("pos:", " ".join(map(str, pos)))
  print()

  n_arvore += 1
