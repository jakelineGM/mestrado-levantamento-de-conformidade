def cria_nodo(valor):
  """Cria um novo nó contendo o valor a ser inserido na pilha.
  """
  nodo = dict()
  # print('cria_nodo', valor)
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

  novo['prox'] = pilha['topo']
  pilha['topo'] = novo
  pilha['tamanho'] += 1
  print(f"push {valor}")


def pop(pilha):
  """Remove um nó do topo da pilha e retorna seu valor.
  """
  if pilha['topo'] is None:
    return False

  valor = peek(pilha)
  pilha['topo'] = pilha['topo']['prox']
  pilha['tamanho'] -= 1
  print(f"pop {valor}")
  return valor

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

def pilha_vazia(pilha):
  return pilha['tamanho'] == 0

pilha = cria_pilha()
while True:
  n = int(input())
  push(pilha, n)
  while pilha['tamanho'] > 1 and peek(pilha) < 0:
    valor1 = pop(pilha)
    valor2 = pop(pilha)
    resultado = valor1 + valor2
    push(pilha, resultado)
  if (not pilha_vazia(pilha) and peek(pilha) == 0) or (peek(pilha) < 0 and pilha['tamanho'] <= 1):
    break