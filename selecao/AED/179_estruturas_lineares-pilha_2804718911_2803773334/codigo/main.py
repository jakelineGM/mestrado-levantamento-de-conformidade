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
  novo = cria_nodo(valor)

  if pilha['topo'] is None:
    pilha['topo'] = novo
  else:
    novo['prox'] = pilha['topo']
    pilha['topo'] = novo
    
  pilha['tamanho'] += 1
  print(f"push {valor}")


def pop(pilha):
  """Remove um nó do topo da pilha e retorna seu valor.
  """
  if pilha['topo'] is None:
    return None

  nodo = pilha['topo']
  pilha['topo'] = nodo['prox']
  pilha['tamanho'] -= 1
  print(f"pop {nodo['valor']}")
  return nodo['valor']


def peek(pilha):
  """Retorna o valor guardado no nó que está no topo da pilha sem
  modificar a pilha. Use para saber se o topo da pilha contém o valor
  zero ou um negativo.
  """
  if pilha['topo'] is None:
    return None
  return pilha['topo']['valor']


def tamanho(pilha):
  """Retorna o número de elementos da pilha. Use para saber se a pilha
  contém elementos suficientes para remover dois de uma vez só.
  """
  return pilha['tamanho']

pilha = cria_pilha()

valor = int(input())

push(pilha, valor)

while peek(pilha) != 0:

  valor = int(input())
  push(pilha, valor)
  
  if peek(pilha) < 0 and tamanho(pilha) > 1:
    #while peek(pilha) < 0 and tamanho(pilha) > 1:
    v1 = pop(pilha)
    v2 = pop(pilha)
    push(pilha, v1 + v2)

  if peek(pilha) < 0 and tamanho(pilha) <= 1:
    break
