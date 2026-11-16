def cria_lista_vazia():
  lista = dict()

  lista['prim'] = None
  lista['fim'] = None
  lista['tamanho'] = 0

  return lista


def insere_fim(lista, valor):
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
  anterior = None
  atual = lista['prim']
  while atual is not None:
    if atual['valor'] == valor:
      if anterior is None:
        lista['prim'] = atual['prox']
        if lista['prim'] is None:
          lista['fim'] = None
      else:
        anterior['prox'] = atual['prox']
        if atual == lista['fim']:
          lista['fim'] = anterior
      lista['tamanho'] -= 1
      return
    anterior = atual
    atual = atual['prox']

def imprime_lista(lista):
  elementos = []
  atual = lista['prim']
  while atual is not None:
    elementos.append(str(atual['valor']))
    atual = atual['prox']
  print(', '.join(elementos) + '.' if elementos else '.')
  
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

imprime_lista(lista)
# continue o código...