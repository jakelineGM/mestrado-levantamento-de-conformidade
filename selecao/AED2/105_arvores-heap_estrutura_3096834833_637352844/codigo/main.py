def max_heapify(vetor, i, tamanho_heap):
  filho_esquerdo = 2*i + 1
  filho_direito = 2*i + 2
  maior = i

  if filho_esquerdo < tamanho_heap and vetor[filho_esquerdo] > vetor[maior]:
    maior = filho_esquerdo
  if filho_direito < tamanho_heap and vetor[filho_direito] > vetor[maior]:
    maior = filho_direito

  if maior != i:
    vetor[i], vetor[maior] = vetor[maior], vetor[i]
    max_heapify(vetor, maior, tamanho_heap)
  
def build_max_heap(vetor):
  tamanho_heap = len(vetor)
  for i in range((tamanho_heap)//2 - 1, -1, -1):
    max_heapify(vetor, i, tamanho_heap)

entrada = eval(input())

while entrada != []:
  build_max_heap(entrada)

  print(entrada)

  entrada = eval(input())
  
  