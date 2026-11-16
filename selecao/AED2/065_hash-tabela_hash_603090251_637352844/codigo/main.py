def funcao_hash(k):
  return k % m

def sondagem_linear(k, i):
  return (funcao_hash(k) + i) % m

m = int(input())
n = int(input())

tabela = []
tamanho_tabela = m

tabela = [-1] * tamanho_tabela

for i in range(n):
  k = 1
  elemento = int(input())
  indice = funcao_hash(elemento)

  while tabela[indice] != -1:
    indice = sondagem_linear(elemento, k)
    k += 1

  tabela[indice] = elemento

for i in range(tamanho_tabela):
  if tabela[i] != -1:
    print("%d: %d" % (i, tabela[i]))

  