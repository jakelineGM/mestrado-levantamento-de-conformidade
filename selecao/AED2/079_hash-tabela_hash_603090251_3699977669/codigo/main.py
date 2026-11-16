def criaTabelaVazia(n):
  tabela = []
  for i in range(n):
    tabela.append(None)
  return tabela

def espalhar(chave, tabelaTamanho):
  return chave % tabelaTamanho
  
def sondar(hash, tabela, tabelaTamanho):
  i = 0
  while tabela[(hash + i) % tabelaTamanho] is not None:
    i += 1
  return (hash + i) % tabelaTamanho

tabelaTamanho = int(input())
itemQuantidade = int(input())

tabela = criaTabelaVazia(tabelaTamanho)

for i in range(itemQuantidade):
  chave = int(input())
  
  hash = espalhar(chave, tabelaTamanho)
  # print("espalhado:", hash)
  hash = sondar(hash, tabela, tabelaTamanho)
  # print("sondado:", hash)
  tabela[hash] = chave
  # print(tabela)

for i in range(tabelaTamanho):
  if tabela[i] is not None:
    print(i, ": ", tabela[i], sep="")
  