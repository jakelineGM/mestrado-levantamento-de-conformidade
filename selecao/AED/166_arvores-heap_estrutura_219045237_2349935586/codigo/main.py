def max_heapify(A, i=0):

  # Tamanho do vetor
  n = len(A)
  indiceEsquerdo = 2*i + 1
  indiceDireito = 2*i + 2
  maior = i

  # Verifica se o filho esquerdo existe e é maior que o pai
  if indiceEsquerdo < n and A[indiceEsquerdo] > A[maior]:
    maior = indiceEsquerdo

  # Verifica se o filho direito existe e é maior que o maior atual
  if indiceDireito < n and A[indiceDireito] > A[maior]:
    maior = indiceDireito

  # Se o maior não for o próprio nó, troca e continua recursivamente
  if maior != i:
    A[i], A[maior] = A[maior], A[i]
    max_heapify(A, maior)

# Entrada dos dados
while True:
  A = eval(input())
  if A == []:
    break # encerra o programa
  max_heapify(A)
  print(A)
  