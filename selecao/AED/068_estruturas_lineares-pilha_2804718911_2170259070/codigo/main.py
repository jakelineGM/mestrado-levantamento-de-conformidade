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

def pop(pilha):
  topo = pilha['topo']
  if topo is None:
    return None

  valor = topo['valor']
  pilha['topo'] = topo['prox']
  pilha['tamanho'] -= 1
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

def processar_entrada(input_data: str):

  numeros = [int(x) for x in input_data.split() if x.strip() !=""]

  pilha = cria_pilha()
  operacoes = []
  parar = False

  for x in numeros:
    if parar:
      break 
    push(pilha, x)
    operacoes.append(f"push {x}")

    while True:
      topo = peek(pilha)

      if topo is None:
        parar = True
        break
        
      if topo == 0:
        parar = True
        break

      if topo < 0: 
        if tamanho(pilha) >= 2:
          v1 = pop(pilha)
          operacoes.append(f"pop {v1}")

          v2 = pop(pilha)
          operacoes.append(f"pop {v2}")

          soma = v1 + v2
          push(pilha, soma)
          operacoes.append(f"push {soma}")

          continue 
        else:
          parar = True
          break
      else:
        break 

  return operacoes

if __name__=="__main__":
  linhas =[]
  while True:
    try:
      linha = input()
    except EOFError:
      break
    if linha.strip() == "":
        break 
    linhas.append(linha)

dados = "\n".join(linhas)
resultados = processar_entrada(dados)
for linha in resultados:
  print(linha)
    
    