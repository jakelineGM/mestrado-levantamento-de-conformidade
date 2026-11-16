def heap_sort(L):
  heap_tam = len(L)
  montar_max_heap(L, heap_tam)
  while heap_tam > 1:
    L[0], L[heap_tam - 1] = L[heap_tam - 1], L[0]
    heap_tam -= 1
    max_heapify(L, 0, heap_tam)

  return L

def montar_max_heap(L, tam):
  ultimo = (tam // 2) - 1
  for i in range(ultimo, -1, -1):
    max_heapify(L, i, tam)

def max_heapify(L, raiz, tam):
  maior = raiz

  esq = (2 * raiz) + 1
  if esq < tam and L[esq] > L[maior]:
    maior = esq

  dir = (2 * raiz) + 2
  if dir < tam and L[dir] > L[maior]:
    maior = dir

  if maior != raiz:
    L[raiz], L[maior] = L[maior], L[raiz]
    max_heapify(L, maior, tam)

vetor = eval(input())
while vetor != []:
  print(heap_sort(vetor))
  vetor = eval(input())