def merge_sort(L):
  if len(L) <=1:
    return L

  meio = len(L) // 2
  esquerda = merge_sort(L[:meio])
  direita = merge_sort(L[meio:])

  return merge(esquerda, direita)

def merge(esq, dir):
  resultado = []
  i = 0 
  j = 0

  while i < len(esq) and j < len(dir):
    if esq[i] <= dir[j]:
      resultado.append(esq[i])
      i+=1
    else:
      resultado.append(dir[j])
      j += 1

  while i < len(esq):
    resultado.append(esq[i])
    i += 1

  while j < len(dir):
    resultado.append(dir[j])
    j += 1

  return resultado

while True:
  entrada = input().strip()
  if entrada == "[]":
    break

  L = eval(entrada)
  L = merge_sort(L)
  print(L)
  