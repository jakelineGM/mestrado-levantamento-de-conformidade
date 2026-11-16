def max_heapify(lista, n, i):

  maior = i
  
  l = 2*i + 1
  if(l < n and lista[l] > lista[maior]):
    maior = l

  r = 2*i + 2
  if(r < n and lista[r] > lista[maior]):
    maior = r

  if maior != i:
    lista[i], lista[maior] = lista[maior], lista[i]
    max_heapify(lista, n, maior)
    
  return lista

def make_heap(lista, n):
  ultimo = (n // 2) - 1
  for i in range(ultimo, -1, -1):
    lista = max_heapify(lista, n, i)
  return lista

def heap_sort(lista):

  tamanho_heap = len(lista)
  lista = make_heap(lista, tamanho_heap)

  while(tamanho_heap > 1):
    lista[0], lista[tamanho_heap - 1] = lista[tamanho_heap-1], lista[0]
    tamanho_heap -= 1
    lista = max_heapify(lista, tamanho_heap, 0)

  return lista

lista = eval(input())

while(lista != []):
  print(heap_sort(lista))
  lista = eval(input())