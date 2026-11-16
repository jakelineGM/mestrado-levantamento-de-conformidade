def max_heapify(vetor, raiz, tam):
  maior = raiz
  esq = 2 * raiz + 1
  dir = 2 * raiz + 2
  if esq < tam and vetor[esq] > vetor[maior]:
    maior = esq
    
  if dir < tam and vetor[dir] > vetor[maior]:
    maior = dir

  if maior != raiz:
    vetor[raiz], vetor[maior] = vetor[maior], vetor[raiz]
    max_heapify(vetor, maior, tam)

def montar_heapMax(vetor, tam):
  ultimo = (tam//2) - 1
  for i in range(ultimo, -1, -1):
    max_heapify(vetor, i, tam)
  return vetor

entrada = eval(input())
while entrada != []:
  print(f"{montar_heapMax(entrada, len(entrada))}")

  entrada = eval(input())
  