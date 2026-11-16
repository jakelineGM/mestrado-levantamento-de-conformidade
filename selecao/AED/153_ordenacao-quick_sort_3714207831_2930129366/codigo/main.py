import ast

def particiona_hoare(L, baixo, alto):
  pivo = L[(baixo+alto)//2]
  i = baixo - 1
  j = alto + 1
  while True:

    i += 1
    while L[i] < pivo:
      i += 1

    j -= 1
    while L[j] > pivo:
      j -= 1

    if i >= j:
      return j

    L[i],L[j] = L[j],L[i]

def quick_sort_intervalo(L, baixo, alto):
  if baixo < alto:
    p = particiona_hoare(L, baixo, alto)
    quick_sort_intervalo(L, baixo, p)
    quick_sort_intervalo(L, p+1, alto)

def quick_sort(L):
  if len(L) > 1:
    quick_sort_intervalo(L, 0, len(L)-1)

while True:
  linha = input().strip()
  if linha == "[]":
    break
  L = ast.literal_eval(linha)
  quick_sort(L)
  print(L)