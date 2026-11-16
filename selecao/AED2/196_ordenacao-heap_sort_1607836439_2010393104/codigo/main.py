def max_heapify(lis, raiz, tam):
  maior = raiz
  
  esq = 2* raiz+1
  if esq < tam and lis[esq]> lis[maior]:
    maior = esq
    
  dir = 2* raiz+2
  if dir < tam and lis[dir]> lis[maior]:
    maior = dir

  if maior != raiz:
    lis[raiz], lis[maior] = lis[maior], lis[raiz]
    max_heapify(lis, maior, tam)

def heap_sort(lis,tam):
  ultimo = (tam//2) - 1
  for i in range(ultimo, -1, -1):
    max_heapify(lis, i, tam)

  for i in range(tam-1, 0, -1):
    lis[0], lis[i] = lis[i], lis[0]
    max_heapify(lis, 0, i)


lis = eval(input())
while lis != []:
   
  heap_sort(lis, len(lis))
  print(lis)

  lis = eval(input())