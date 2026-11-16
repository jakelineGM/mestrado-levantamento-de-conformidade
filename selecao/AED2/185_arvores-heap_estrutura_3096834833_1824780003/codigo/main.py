def Max_Heapify(a, i = 0):
  n = len(a)
  esquerda = 2 * i + 1
  direita = 2 * i + 2
  maior = i

  if esquerda < n and a[esquerda] > a[maior]:
    maior = esquerda

  if direita < n and a[direita] > a[maior]:
    maior = direita

  if maior != i:
    a[i], a[maior] = a[maior], a[i]
    Max_Heapify(a, maior)

while True:
  entrada = input().strip()
  if entrada == "[]":
    break
  a = eval(entrada)
  Max_Heapify(a)
  print(a)