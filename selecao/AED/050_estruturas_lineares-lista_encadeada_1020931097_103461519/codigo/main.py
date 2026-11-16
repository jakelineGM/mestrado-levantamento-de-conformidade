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
  if lista['prim'] is None:
    lista['prim'] = programa
    programa['ant'] = programa
    programa ['prox'] = programa
  else : 
    ultimo = lista ['prim']['ant']
    ultimo ['prox'] = programa
    programa['ant'] = ultimo
    programa['prox'] = lista['prim']
    lista['prim']['ant'] = programa
  lista['num_programas'] += 1



def remove(lista, programa):
  """Remove um programa (nó) da lista encadeada.
  """ 
  if lista['prim'] is None:
    return
  if lista['prim'] == programa:
    if lista['prim'] == lista['prim'] ['ant']:
      lista['prim']  = None
    else:
      lista['prim'] = programa ['prox']
      lista['prim'] ['ant'] = programa ['ant']
      programa ['ant'] ['prox'] = lista ['prim']
  else:  
    programa['ant']['prox'] = programa ['prox']
    programa['prox']['ant'] = programa ['ant']
    
  lista['num_programas'] -= 1

'''def imprime_lista (lista):
  ponteiro = lista['prim']
  for i in range(lista['num_programas']):
      print(ponteiro['nome'] , ponteiro['tempo_restante'])
      ponteiro = ponteiro['prox']
'''

def simula_execucao(cota, lista):
  tempo_atual = 0
  programa = lista['prim']

  while lista['num_programas'] > 0 :
    tempo_usado = min(cota, programa['tempo_restante'])
    tempo_atual += tempo_usado
    programa['tempo_restante'] -= tempo_usado
    
    if programa['tempo_restante'] == 0:
        print(f"{tempo_atual} us: {programa['nome']} finalizou")
        remove(lista, programa)

    if lista['num_programas'] > 0:
      programa =programa['prox']
      
  print(f"{tempo_atual} us: shutdown")  
  
  
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


simula_execucao(cota, lista)

# Agora é com você! Simule a execução de todos os programas, manipulando corretamente
# a lista circular e imprimindo sempre que um programa finaliza sua execução