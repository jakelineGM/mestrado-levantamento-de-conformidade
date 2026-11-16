def max_heapify(qheap, raiz, tamanho):
 
  maior = raiz
  esq = (2 * raiz) + 1
  dir = (2 * raiz) + 2
  
  if esq < tamanho and qheap[esq] > qheap[maior]:
     maior = esq

  if dir < tamanho and qheap[dir] > qheap[maior]:
     maior = dir

  if maior != raiz:
     qheap[raiz], qheap[maior] = qheap[maior], qheap[raiz]
     max_heapify(qheap, maior, tamanho)

    

vetor = eval(input())

while vetor != []:
  
  tamanho = len(vetor)

  for i in range(tamanho // 2 - 1, -1, -1):
      max_heapify(vetor, i, tamanho)
    
  print(vetor)
  
  vetor = eval(input())
  
  

  