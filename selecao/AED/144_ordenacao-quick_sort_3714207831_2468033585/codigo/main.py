def particao_hoare(L, inicio, fim):
  pivo = lista[(inicio + fim) // 2]
  i = inicio - 1
  j = fim + 1

  while True:
    i += 1
    while lista[i] < pivo:
      i += 1

    j -= 1
    while lista[j] > pivo:
      j -= 1

    if i >= j:
      return j

    lista[i], lista[j] = lista[j], lista[i]

def quick_sort_recursivo(lista, inicio, fim):
  if inicio < fim:
    posicao = particao_hoare(lista, inicio, fim)
    quick_sort_recursivo(lista, inicio, posicao)
    quick_sort_recursivo(lista, posicao+1, fim)

def quick_sort(lista):
  if len(lista) > 1:
    quick_sort_recursivo(lista, 0, len(lista) -1)

while True:
  entrada = input()

  if entrada == "[]":
    break

  lista = eval(entrada)
  quick_sort(lista)
  print(lista)