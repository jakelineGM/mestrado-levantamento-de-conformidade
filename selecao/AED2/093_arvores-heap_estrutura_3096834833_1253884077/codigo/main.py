def max_heapify(vetor, raiz, tam):
  maior = raiz
  esq = 2*raiz+1
  if esq < tam and vetor[esq] > vetor[maior]:
    maior = esq

  dir = 2*raiz+2
  if dir < tam and vetor[dir] > vetor[maior]:
    maior = dir

  if maior != raiz:
    vetor[raiz], vetor[maior] = vetor[maior], vetor[raiz]
    max_heapify(vetor, maior, tam)

entrada = eval(input())

while entrada != []:
  tam = len(entrada)
  max_heapify(entrada, 0, tam)
  print(entrada)

  entrada = eval(input())