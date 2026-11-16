def max_heapify(lista, i):

  n = len(lista)
  
  maior = i
  esq = 2 * i + 1
  dir = 2 * i + 2

  if esq < n and lista[esq] > lista[maior]:
    maior = esq

  if dir < n and lista[dir] > lista[maior]:
    maior = dir

  if maior != i:
    lista[i], lista[maior] = lista[maior], lista[i]
    max_heapify(lista, maior)


lista = eval(input())

while len(lista) > 0:
  max_heapify(lista, 0)
  print(lista)

  lista = eval(input())