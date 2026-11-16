def max_heapify(A):
  n = len(A)
  if n == 0:
    return
  i = 0
  while True:
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and A[esq]> A[maior]:
      maior = esq
    if dir < n and A[dir] > A[maior]:
      maior = dir
    if maior != i:
      A[i], A[maior] = A[maior], A[i]
      i = maior
    else:
      break
entrada = ""
while True:
  entrada = input()
  if entrada.strip() == "[]":
    break
  try:
    lista = eval(entrada)
    if not isinstance(lista, list):
      raise ValueError("")
    max_heapify(lista)
    print(lista)
  except Exception as e:
    print("", e)