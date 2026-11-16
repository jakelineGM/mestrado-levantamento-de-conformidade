m = int(input())
n = int(input())

tabela = [None] * m

for j in range(n):
  k = int(input())

  for i in range(m):
    posicao = (k + i) % m
    if tabela[posicao] is None:
      tabela[posicao] = k
      break

for indice in range(m):
  if tabela[indice] is not None:
    print(f"{indice}: {tabela[indice]}")