def max_heapify(A, i=0):

  # Tamanho do vetor
  n = len(A)
  indiceEsquerdo = 2*i + 1
  indiceDireito = 2*i + 2
  maior = i

  if indiceEsquerdo < n and A[indiceEsquerdo] > A[maior]:
    maior = indiceEsquerdo

  if indiceDireito < n and A[indiceDireito] > A[maior]:
    maior = indiceDireito

  if maior != i:
    A[i], A[maior] = A[maior], A[i]
    max_heapify(A, maior)

# Entrada
while True:
  A = eval(input())
  if A == []:
    break
  max_heapify(A)
  print(A)
  