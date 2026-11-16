def max_heapify(heap, raiz, tam):
  maior = raiz

  esq = 2*raiz +1
  # Se tem filho esquerdo e esse filho eh maior q heap[maior] 
  if((esq < tam) and (heap[esq] > heap[maior])):
    maior = esq

  dir = 2*raiz +2
  # Se tem filho direito e esse filho eh maior q p heap[maior]
  if((dir < tam) and (heap[dir] > heap[maior])):
    maior = dir

  # Caso for nessesaria uma troca com a raiz
  # aplicamos max_heapify para nao baguncar a heap
  if(maior != raiz):
    heap[raiz], heap[maior] = heap[maior], heap[raiz]
    max_heapify(heap, maior, tam)
    
  return heap

def montar_heap(lst):
  mid = len(lst)//2

  # Aplicar max heapify da direita para a esq
  for i in range(mid-1, -1, -1):
    lst = max_heapify(lst, i, len(lst))

  return lst
  
def heapSort(lst):

  heap = montar_heap(lst)
  tam = len(heap)

  while(tam):
    
    # Troca o prim com o ult
    lst[0], lst[tam-1] = lst[tam-1], lst[0]
    
    # Remove o ult elem da heap
    tam -= 1

    # Max_heapify na heap
    heap = max_heapify(heap, 0, tam)
    
  return lst
    
lst = eval(input())
while(lst):

  lst = heapSort(lst)
  print(lst)  

  lst = eval(input())