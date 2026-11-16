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
    else:      
      lista['fim']['prox'] = novo
      lista['fim'] = novo
    lista['tamanho'] += 1


def remove(lista, valor):
    """Procura e remove a primeira ocorrência de um nó que possui o valor
    especificado pelo parâmetro.
    """
    # continue o código
    if lista['prim'] is not None:
      atual = lista['prim']
      if (atual['valor'] == valor):
        lista['prim'] = atual['prox']
        atual['prox'] = None
        lista['tamanho'] -= 1
        if lista['fim'] == atual:
          lista['fim'] = lista['prim']
      else:              
        while atual['prox'] is not None:
          ant = atual
          atual = atual['prox']
          if atual['valor'] == valor:
            if atual == lista['fim']:
                lista['fim'] = ant
            ant['prox'] = atual['prox']
            atual['prox'] = None
            lista['tamanho'] -= 1
            break

def imprimir(lista):
  atual = lista['prim']
  saida = []
  while atual is not None:
    saida += [str(atual['valor'])]
    atual = atual['prox']
  print(', '.join(saida), end='.\n')


# Programa principal
lista = cria_lista_vazia()

# Lê os números que precisam ser inseridos na lista
inserir = input().split(' ')
for i in inserir:
    insere_fim(lista, int(i))

# Lê os números que devem ser removidos da lista
remover = input().split(' ')
for r in remover:
    remove(lista, int(r))

# continue o código...
imprimir(lista)