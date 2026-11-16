def max_heapify(l, raiz, tam):
  maior = raiz

  esq = 2 * raiz + 1
  if esq < tam and l[esq] > l[maior]:
    maior = esq
  
  dire = 2 * raiz + 2
  if dire < tam and l[dire] > l[maior]:
    maior = dire

  if maior != raiz:
    l[raiz], l[maior] = l[maior], l[raiz]
    max_heapify(l, maior, tam)

def montar_max_heap(l, tam):
  ultimo = (tam//2) - 1
  for i in range(ultimo, -1, -1):
    max_heapify(l, i, tam)

def heap_sort(l):
  tamanho_heap = len(l)
  montar_max_heap(l, tamanho_heap)
  while tamanho_heap > 1:
    l[0], l[tamanho_heap - 1] = l[tamanho_heap - 1], l[0]
    tamanho_heap -= 1
    max_heapify(l, 0, tamanho_heap)
  print(l)

while True:
  l = eval(input())
  if l == []:
    break
  heap_sort(l)
