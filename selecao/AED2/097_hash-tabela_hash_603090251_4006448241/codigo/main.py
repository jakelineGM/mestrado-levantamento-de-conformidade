m = int(input())
n = int(input())

tabela = [None] * m

for i in range(n):
  numeros = int(input())

  j = 0
  posicao = numeros % m
  while tabela[posicao] != None:
    j = j + 1
    posicao = (numeros + j) % m
  tabela[posicao] = numeros

for pos in range(m):
  if tabela[pos] != None:
    print("%d: %d"  % (pos, tabela[pos]))