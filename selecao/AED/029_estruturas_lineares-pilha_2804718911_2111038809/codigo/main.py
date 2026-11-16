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
  print('push {}'.format(valor))

def pop(pilha):
  """Remove um nó do topo da pilha e retorna seu valor.
  """
  if pilha['tamanho'] == 0:
    return None

  topo = pilha['topo']
  pilha['topo'] = topo['prox']
  pilha['tamanho'] -= 1
  print('pop {}'.format(topo['valor']))
  return topo['valor']
  

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

def process_data():
  pilha = cria_pilha()

  num = input()
  if num != '':
    num = int(num)
    push(pilha, num)


  while True:
    if peek(pilha) == 0:
      break

    if peek(pilha) < 0:
      if (tamanho(pilha) < 2):
        break
      else:
        value1 = pop(pilha)
        value2 = pop(pilha)
        push(pilha, (value1+value2))

    if peek(pilha) > 0:
        num = input()
        if num == '':
          break
        else:
          num = int(num)
          push(pilha, num)

process_data()
  