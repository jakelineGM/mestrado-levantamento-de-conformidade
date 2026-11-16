def max_heapify(A, n, i):
  esq = 2 * i + 1
  dir = 2 * i + 2
  maior = i

  if esq < n and A[esq] > A[maior]:
    maior = esq

  if dir < n and A[dir] > A[maior]:
    maior = dir

  if maior != i:
    A[i], A[maior] = A[maior], A[i]
    max_heapify(A, n, maior)

def transformar_em_max(A):
  n = len(A)
  for i in range(n//2 - 1,-1,-1):
    max_heapify(A,n,i)
  return A

while True:
  lista = input()
  try:
    lista=eval(lista)
    if lista == []:
      break

    lista_heap = transformar_em_max(lista)
    print(lista_heap)

  except:
    print("Entrada inválida")
    