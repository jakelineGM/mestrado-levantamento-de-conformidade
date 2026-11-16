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
  novo['prox'] = pilha['topo']
  pilha['topo'] = novo
  pilha['tamanho'] += 1
  print(f"push {valor}")

def pop(pilha):
  """Remove um nó do topo da pilha e retorna seu valor.
  """
  if pilha['topo'] is None:
    return None

  valor = pilha['topo']['valor']
  pilha['topo'] = pilha['topo']['prox']
  pilha['tamanho'] -= 1
  print(f"pop {valor}")
  return valor

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

while True:
  if peek(pilha) is None or peek(pilha) > 0:
    numero = int(input())
    push(pilha, numero)
  else:
    break
  
  while peek(pilha) is not None and peek(pilha) < 0:
    if pilha['tamanho'] < 2:
      break

    primeiro = pop(pilha)
    segundo = pop(pilha)

    if primeiro is None or segundo is None:
      break

    soma = primeiro + segundo
    push(pilha, soma)
    
  if peek(pilha) == 0:
      break




