from sys import stdin

def cria_nodo(valor):
  """Cria um novo nó contendo o valor a ser inserido na pilha.
  """
  nodo = dict()

  nodo['valor'] = valor
  nodo['prox'] = None

  return nodo


def cria_pilha():
  """Cria uma pilha inicialmente vazia.
  """
  pilha = dict()

  pilha['topo'] = None
  pilha['tamanho'] = 0

  return pilha


def push(pilha, valor):
  """Cria um nó contendo o valor especificado pelo parâmetro e o insere
  no topo da pilha.
  """
  print("push %d"%(valor))
  novo = cria_nodo(valor)

  novo['prox'] = pilha['topo']
  pilha['topo'] = novo
  pilha['tamanho'] += 1


def pop(pilha):
  """Remove um nó do topo da pilha e retorna seu valor.
  """

  print("pop %d"%(peek(pilha)))
  pilha['topo'] = pilha['topo']['prox']
  pilha['tamanho'] -= 1


def peek(pilha):
  """Retorna o valor guardado no nó que está no topo da pilha sem
  modificar a pilha. Use para saber se o topo da pilha contém o valor
  zero ou um negativo.
  """

  return pilha['topo']['valor']


def tamanho(pilha):
  """Retorna o número de elementos da pilha. Use para saber se a pilha
  contém elementos suficientes para remover dois de uma vez só.
  """
  return pilha['tamanho']

pilha = cria_pilha()

while True:
  try:
    line = input()
    if line == '':
      break
    n = int(line)
    push(pilha, int(n))
  
    while peek(pilha) < 0 and tamanho(pilha) >= 2:
      a = peek(pilha)
      pop(pilha)
      b = peek(pilha)
      pop(pilha)
      push(pilha, a+b)

      if peek(pilha) == 0:
        break
    if peek(pilha) == 0 or tamanho(pilha) < 2 and peek(pilha) < 0:
      break
  
  except EOFError:
    break
    