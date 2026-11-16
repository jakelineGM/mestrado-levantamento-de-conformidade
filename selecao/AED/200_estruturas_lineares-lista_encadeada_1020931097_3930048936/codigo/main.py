def cria_programa(nome, tempo_restante):
  """Cria um dicionário que representa um nó da lista duplamente encadeada, inicialmente
  apontando para None. Você deve ajustar as referências para inserir este nó na lista.
  """
  programa = dict()

  programa['nome'] = nome
  programa['tempo_restante'] = tempo_restante

  programa['ant'] = None
  programa['prox'] = None

  return programa


def cria_lista():
  """Cria um dicionário que representa uma lista circular inicialmente vazia.
  """
  lista = dict()

  lista['prim'] = None
  lista['num_programas'] = 0

  return lista


def insere_fim(lista, programa):
  """Insere um nó (programa) no fim da lista. O parâmetro programa é uma
  referência para um nó criado pela função cria_programa().
  """
  
  # Lista está vazia
  if lista['prim'] is None:
    lista['prim'] = programa
    programa['prox'] = lista['prim']
    programa['ant'] = lista['prim']
  # Lista possui somente um nó
  elif lista['prim']['ant'] is None:
    lista['prim']['ant'] = programa
    programa['prox'] = lista['prim']
    lista['prim']['prox'] = programa
    programa['ant'] = lista['prim']
  # Lista possui mais de 1 nó
  else:
    # Salva o antigo último nó
    programaAnterior = lista['prim']['ant']
    # Atualiza o novo último nó
    lista['prim']['ant'] = programa
    programa['prox'] = lista['prim']
    # Manipulações envolvendo o antigo último nó
    programa['ant'] = programaAnterior
    programaAnterior['prox'] = programa
  lista['num_programas'] += 1
    
def remove(lista, programa, tempoTotal):
  """Remove um programa (nó) da lista encadeada.
  """ 
  if programa is lista['prim']:
    # Quando existir somente um nó na lista
    if lista['num_programas'] == 1:
      lista['prim']['prox'] = None
      lista['prim']['ant'] = None
      lista['prim'] = None
    else:
      lista['prim'] = lista['prim']['prox']
      lista['prim']['ant'] = programa['ant']
      programa['ant']['prox'] = lista['prim']
  else:
    programa['prox']['ant'] = programa['ant']
    programa['ant']['prox'] = programa['prox']
  lista['num_programas'] -= 1

  print("%d us: %s finalizou" % (tempoTotal, programa['nome']))

def rodar_programas(lista, cota):
  tempoTotal = 0
  atual = lista['prim']
  # Fica em loop até a lista ficar vazia
  while atual is not None:
    atual['tempo_restante'] -= cota
    tempoTotal += cota
    # Esta condição simula a distribuição de excesso de tempo
    # de um dado programa para um outro programa
    if atual['tempo_restante'] < 0:
      tempoTotal += atual['tempo_restante']
    # Programa finalizou
    if atual['tempo_restante'] <= 0:
      remove(lista, atual, tempoTotal)
    atual = atual['prox']
  print("%d us: shutdown" % tempoTotal)

# Lê as configurações do exercício
cota, num_programas = map(int, input().split(' '))

# Cria uma lista ligada vazia
lista = cria_lista()

# Lê os programas e os insere na lista
for _ in range(num_programas):
  nome, tempo_total_string = input().split(' ')

  # Cria um nó para o programa
  programa = cria_programa(nome, int(tempo_total_string))

  # Insere o programa (nó) no final da lista ligada
  insere_fim(lista, programa)

# Simula a execução de um conjunto de programas
rodar_programas(lista, cota)
# Agora é com você! Simule a execução de todos os programas, manipulando corretamente
# a lista circular e imprimindo sempre que um programa finaliza sua execução