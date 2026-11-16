m = int(input())

n = int(input())

tabela = [None] * m

for i in range(n):
  k = int(input())
  
  i = 0
  pos = (k + i) % m

  while tabela[pos] != None:
    i += 1
    pos = (k + i) % m

  tabela[pos] = k

for i in range(m):
  if tabela[i] is not None:
    print(f"{i}: {tabela[i]}")



