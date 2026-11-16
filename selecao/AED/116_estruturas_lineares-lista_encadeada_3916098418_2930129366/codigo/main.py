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
    anterior = None
    atual = lista['prim']

    while atual is not None:
      if atual['valor'] == valor:
        if anterior is None:
          lista['prim'] = atual['prox']
        else:
          anterior['prox'] = atual['prox']

        if atual is lista['fim']:
          lista['fim'] = anterior
          
        lista['tamanho'] -=1
        return True
      anterior = atual
      atual = atual['prox']
    return False
          

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

atual = lista['prim']
saida = []
while atual is not None:
  saida.append(str(atual['valor']))
  atual = atual['prox']
print(', '.join(saida) + '.' if saida else '.')