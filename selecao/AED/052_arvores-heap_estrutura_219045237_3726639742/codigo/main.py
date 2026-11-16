def max_heapify(A, i, n):
  largest =  i
  esquerda = 2 * i +1
  direita = 2 * i + 2

  if esquerda < n and A[esquerda] > A[largest]:
    largest = esquerda

  if direita < n and A[direita] > A[largest]:
    largest = direita

  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    max_heapify(A, largest, n)

def heapify(A):
  tamanho = len(A)
  max_heapify(A, 0, tamanho)

if __name__ == "__main__":
  while True:
    entrada = input()
    if entrada == "[]":
      break
    lista = eval(entrada)
    heapify(lista)
    print(lista)