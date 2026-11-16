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

  # Insira o novo nó na pilha...
  novo['prox'] = pilha['topo']
  pilha['topo'] = novo
  pilha['tamanho'] += 1

  # Saída
  print(f"push {valor}")


def pop(pilha):
  """Remove um nó do topo da pilha e retorna seu valor.
  """
  if pilha['tamanho'] == 0:
    return None

  nodo_removido = pilha['topo']
  valor = nodo_removido['valor']

  # Atualiza o topo para o próximo nó
  pilha['topo'] = nodo_removido['prox']
  pilha['tamanho'] -= 1

  # Saída
  print(f"pop {valor}")
  return valor


def peek(pilha):
  """Retorna o valor guardado no nó que está no topo da pilha sem
  modificar a pilha. Use para saber se o topo da pilha contém o valor
  zero ou um negativo.
  """
  if pilha['tamanho'] == 0:
    return None

  return pilha['topo']['valor']

def tamanho(pilha):
  """Retorna o número de elementos da pilha. Use para saber se a pilha
  contém elementos suficientes para remover dois de uma vez só.
  """
  return pilha['tamanho']


# Lógica principal
def main():
  
  minha_pilha = cria_pilha()
  lista_entradas = []

  # Lê a entrada 
  while True:
    try:
      n = int(input())
      lista_entradas.append(n)
    except (ValueError, EOFError):
      break
  
  # Processar operações
  for n in lista_entradas:
    push(minha_pilha, n)

    # Loop de verificação de regras
    while True:
      topo_valor = peek(minha_pilha)

      if topo_valor is None:
        break
        
      # Condição de parada -> topo é zero
      if topo_valor == 0:
        return

      # Verifica se topo é negativo
      if topo_valor < 0:
        if tamanho(minha_pilha) >= 2:
          v1 = pop(minha_pilha) # O negativo (topo)
          v2 = pop(minha_pilha) # O anterior
          
          soma = v1 + v2
          push(minha_pilha, soma)
        else:
          return
      else:
        break

main()