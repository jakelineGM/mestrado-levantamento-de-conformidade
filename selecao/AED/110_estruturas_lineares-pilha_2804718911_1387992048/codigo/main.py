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

  topo = pilha['topo']
  pilha['topo'] = topo['prox']
  pilha['tamanho'] -= 1
  print(f"pop {topo['valor']}")
  return topo['valor']

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

def processa_pilha():

  pilha = cria_pilha()
  canBreak = False
  
  while True:
    entrada = input().strip()

    if entrada == "":
      break
    
    valor = int(entrada)

    if valor >= 0 and peek(pilha) != 0:
      push(pilha,valor)
      # break
      
    if pilha['tamanho'] > 0 and peek(pilha) == 0:
      break
    
    if valor < 0:
      push(pilha, valor)  
      if pilha['tamanho'] >= 2:
        v1 = pop(pilha)
        v2 = pop(pilha)
        soma = v1+v2
        push(pilha, soma)
      else:
        break

    #print('here')
    #print('tam ', pilha['tamanho'])
    #print('peek ', peek(pilha))
        
    while pilha['tamanho'] > 0 and peek(pilha) < 0:
      ## pega os 2
      if pilha['tamanho'] >= 2:
        v1 = pop(pilha)
        v2 = pop(pilha)
        soma = v1+v2
        push(pilha, soma)
      else:
        ## nao consigo fazer entao acaba
        canBreak = True
        break
      #print('there ', peek(pilha))

    if peek(pilha) == 0 or canBreak:
        return
    
processa_pilha()
