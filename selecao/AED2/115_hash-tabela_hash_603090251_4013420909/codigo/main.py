def espalhamento(k, m):
  return k % m

def sondagem_linear(k, i, m):
  return (k + i) % m

tamanhoTabela =  int(input())
quantidadeValoresTabela = int(input())

tabela = []

for i in range(tamanhoTabela):
  tabela.append(None)

j = 0
while j < quantidadeValoresTabela:
  chave = int(input())
  indiceChave = espalhamento(chave, tamanhoTabela)

  if tabela[indiceChave] == None:
    tabela[indiceChave] = chave
  else:
    i = 1
    while (tabela[indiceChave] != None) and (i < quantidadeValoresTabela):
      indiceChave = sondagem_linear(chave, i, tamanhoTabela)
      i += 1
    tabela[indiceChave] = chave
    
  j+=1
  
for i in range(tamanhoTabela):
  if tabela[i] != None:
    print("%d: %d" % (i, tabela[i]))
#print(tabela)    
  