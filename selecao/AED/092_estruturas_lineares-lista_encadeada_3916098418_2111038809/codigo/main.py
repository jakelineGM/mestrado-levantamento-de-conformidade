def cria_lista_vazia():
    """Cria uma lista vazia. A lista será um dicionário que contém uma referência
    para o primeiro elemento e uma referência para o último elemento (inicialmente
    None), além de um contador do número de nós.
    """
    lista = dict()

    lista['prim'] = None
    lista['fim'] = None
    lista['tamanho'] = 0

    return lista

def insere_fim(lista, valor):
  """Insere um novo elemento no fim da lista. Não se esqueça de ajustar o
  contador do número de elementos.
  """
  novo = dict()
  novo['valor'] = valor
  novo['prox'] = None

  if lista['prim'] is None:
    lista['prim'] = novo
    lista['fim'] = novo
    lista['tamanho'] += 1
  else:
    lista['fim']['prox'] = novo
    lista['fim'] = novo
    lista['tamanho'] += 1

  return lista
    
def remove(lista, valor):
  """Procura e remove a primeira ocorrência de um nó que possui o valor
    especificado pelo parâmetro.
  """
  if lista['tamanho'] == 0:
    return lista
  elif lista['tamanho'] == 1:
    lista['prim'] == None
    lista['fim'] == None
    lista['tamanho'] -= 1
  elif valor == lista['prim']['valor']:
    aux = lista['prim']
    lista['prim'] = aux['prox']
    aux = None
    lista['tamanho'] -= 1
  else:
    ultimo = lista['prim']
    penultimo = None
    
    while ultimo['valor'] != valor:
      penultimo = ultimo
      ultimo = ultimo['prox']

    if ultimo['prox'] is None:
      lista['fim'] = penultimo
      penultimo['prox'] = None
      ultimo = None
      lista['tamanho'] -= 1
    else:
      penultimo['prox'] = ultimo['prox']
      ultimo = None
      lista['tamanho'] -= 1
  
  return lista

def mostrar_lista_final(lista: dict):
  # print(lista)
  if lista['tamanho'] == 0:
    print('.')
  else:
    aux = lista['prim']
    while aux['prox'] != None:
      print(aux['valor'], end=', ')
      aux = aux['prox']
      
    print(str(aux['valor']) + '.')
  
# Programa principal
lista = cria_lista_vazia()

# Lê os números que precisam ser inseridos na lista
inserir = input().split(' ')
for i in inserir:
    lista = insere_fim(lista, int(i))


# Lê os números que devem ser removidos da lista
remover = input().split(' ')
for r in remover:
    lista = remove(lista, int(r))


mostrar_lista_final(lista)