def cria_lista_vazia():
    lista = dict()

    lista['prim'] = None
    lista['fim'] = None
    lista['tamanho'] = 0

    return lista


def push(lista, valor):
    novo = dict()
    novo['valor'] = valor
    novo['prox'] = None

    if lista['fim'] is not None:
      lista['fim']['prox'] = novo
    else:
      lista['prim'] = novo
    lista['fim'] = novo
    lista['tamanho'] +=1
    return lista
  
def pop(lista):
  aux = None
  if lista['tamanho'] > 0:
    aux = lista['prim']['valor']
    lista['tamanho'] -= 1
    lista['prim'] = lista['prim']['prox']
    if lista['prim'] is None:
      lista['fim'] = None
  return aux

entradas = input().split()
entradas = list(map(int, entradas))
for e in entradas:
  if e > 0:
    lista = cria_lista_vazia()
    for carta in range(e):
      push(lista, carta+1)
    descartadas = []
    while lista['tamanho'] > 1:
      descartadas.append(pop(lista))
      push(lista, pop(lista))
    print("Descartadas:", *descartadas)
    print("Restou:", pop(lista))