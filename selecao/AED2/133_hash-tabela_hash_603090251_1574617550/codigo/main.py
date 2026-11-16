def hash(k, m):
  return k%m

def hash_linha(k, i, m):
  return (k + i)%m

tamanho = eval(input())
quantidade = eval(input())
tabela = [-1]*tamanho

for i in range(quantidade):
  num = eval(input())
  indiceInsercao = hash(num, tamanho)

  if tabela[indiceInsercao] == -1:
    tabela[indiceInsercao] = num
  else:
    j = 0
    while tabela[indiceInsercao] != - 1:
      indiceInsercao = hash_linha(num, j, tamanho)
      j+=1
    tabela[indiceInsercao] = num

for i in range(tamanho):
  if tabela[i] != -1:
    print(f"{i}: {tabela[i]}")