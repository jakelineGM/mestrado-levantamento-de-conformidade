def max_heapify(vet,raiz,tam):
  maior = raiz

  esq = 2*raiz+1
  if esq < tam and vet[esq] > vet[maior]:
    maior = esq

  dir = 2*raiz+2
  if dir < tam and vet[dir] > vet[maior]:
    maior = dir

  if raiz != maior:
    aux = vet[raiz]
    vet[raiz] = vet[maior]
    vet[maior] = aux
    max_heapify(vet,maior,tam)

def heap_max(vet):
  tam = len(vet)
  for i in range(tam-1,-1,-1):
    max_heapify(vet,i,tam)

def heap_sort(vet):
  tam = len(vet)
  heap_max(vet)

  for i in range(tam-1,-1,-1):
    aux = vet[0]
    vet[0] = vet[i]
    vet[i]=aux
    max_heapify(vet,0,i)

entrada = eval(input())

while entrada != []:
  heap_sort(entrada)
  print(entrada)

  entrada = eval(input())
    
  