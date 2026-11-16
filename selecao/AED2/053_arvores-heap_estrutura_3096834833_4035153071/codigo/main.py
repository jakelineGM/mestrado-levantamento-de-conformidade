def max_heapfy(lista, raiz, tama):
  maior = raiz

  left = 2 * raiz + 1
  if left < tama and lista[left] > lista[maior]:
    maior = left

  right = 2 * raiz + 2
  if right < tama and lista[right] > lista[maior]:
    maior = right

  if maior != raiz:
    lista[raiz], lista[maior] = lista[maior], lista[raiz]
    max_heapfy(lista, maior, tama)

entrada = eval(input())

while entrada != []:
  max_heapfy(entrada, 0, len(entrada))
  print(entrada)
  entrada = eval(input())