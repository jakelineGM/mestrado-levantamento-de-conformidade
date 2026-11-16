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


lis = eval(input())
while lis != []:
   
  max_heapify(lis, 0, len(lis))

  print(lis)

  lis = eval(input())
  