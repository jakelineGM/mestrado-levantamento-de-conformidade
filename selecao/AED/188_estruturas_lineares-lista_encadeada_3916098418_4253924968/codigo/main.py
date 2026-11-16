def cria_lista_vazia():
    """Cria uma lista vazia. A lista será um dicionário que contém uma referência
    para o primeiro elemento e uma referência para o último elemento (inicialmente
    None), além de um contador do número de nós.
    """
    lista = dict()
    lista['prim'] = None
    lista['fim'] = None
    lista['num'] = 0
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
    else:
      lista['fim']['prox'] = novo
      lista['fim'] = novo
    lista['num'] += 1
      

def remove(lista, valor):
    """Procura e remove a primeira ocorrência de um nó que possui o valor
    especificado pelo parâmetro.
    """
    # continue o código
    sentinela = {'prox': lista['prim']}
    ant = sentinela
    atual = lista['prim']
    while atual is not None and atual['valor'] != valor:
      ant = atual
      atual = atual['prox']

    if atual is None:
      return
    
    ant['prox'] = atual['prox']
    lista['prim'] = sentinela['prox']
  
    if atual == lista['fim']:
      if ant is sentinela:
        lista['fim'] = None
      else:
        lista['fim'] = ant
    lista['num'] -= 1

def imprime_lista(lista):
  atual = lista['prim']
  saida = []
  while atual is not None:
    saida.append(str(atual['valor']))
    atual = atual['prox']
  if saida:
    print(', '. join(saida) + '.')
  else:
    print('.')


# Programa principal
lista = cria_lista_vazia()

# Lê os números que precisam ser inseridos na lista
inserir = input().split(' ')
for i in inserir:
  if i != '':
    insere_fim(lista, int(i))


# Lê os números que devem ser removidos da lista
remover = input().split(' ')
for r in remover:
  if r != '':
    remove(lista, int(r))

imprime_lista(lista)
# continue o código...