def heap_sort(L):
  build_max_heap(L)
  n = len(L)
  for i in range(n-1, 0, -1):
    L[0], L[i] = L[i], L[0]
    max_heapify(L, i, 0)

# Executa o max_heapify do 1º item da penúltima linha para cima
def build_max_heap(L):
  n = len(L)

  # ((n // 2) - 1) --> encontra o índice do 1º item da penúltima linha
  for i in range((n // 2) - 1, -1, -1):

    # Executa o max_heapify do índice i até o índice 0 (decrescente)
    max_heapify(L, n, i)

def max_heapify(A, n, i=0):

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
    max_heapify(A, n, maior)

# Entrada dos dados
while True:
  L = eval(input())
  if L == []:
    break # encerra o programa
  heap_sort(L)
  print(L)