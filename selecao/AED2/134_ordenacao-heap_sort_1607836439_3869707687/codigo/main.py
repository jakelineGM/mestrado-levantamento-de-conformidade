def max_heapify(lista, raiz, n):
  maior = raiz
  esq = 2 * raiz + 1
  dir = 2 * raiz + 2
  
  if esq < n and lista[esq] > lista[maior]:
    maior = esq
  
  if dir < n and lista[dir] > lista[maior]:
    maior = dir
  
  if maior != raiz:
    lista[raiz], lista[maior] = lista[maior], lista[raiz]
    max_heapify(lista, maior, n)
    
def montar_max_heap(lista, n):
  ultimo = (n // 2) - 1
  for i in range(ultimo, -1, -1):
    max_heapify(lista, i, n)
  
def heap_sort(lista, n):
  if n <= 1:
    return
    
  montar_max_heap(lista,n)

  for i in range(n - 1, 0, -1):
    lista[0], lista[i] = lista[i], lista[0]

    max_heapify(lista, 0, i)
while True:
  lista = eval(input())

  if lista == []:
    break

  n = len(lista)
  heap_sort(lista, n)

  print(lista)