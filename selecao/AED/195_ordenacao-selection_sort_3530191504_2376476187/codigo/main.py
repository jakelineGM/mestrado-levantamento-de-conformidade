lista = eval(input())
tamanho = len(lista)
i = 0

while i < (tamanho - 1):
  posicao_menor = i
  j = i + 1

  while j < tamanho:
    if lista[j] < lista[posicao_menor]:
      posicao_menor = j

    j += 1

  if i != posicao_menor:
    print(f"{lista[i]} <-> {lista[posicao_menor]}")
    lista[i], lista[posicao_menor] = lista[posicao_menor], lista[i]

  i += 1

print(lista)
