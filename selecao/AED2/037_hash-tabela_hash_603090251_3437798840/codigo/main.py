tabelaTam= int(input())
chaves= int(input())

tabela=[None] * tabelaTam

for i in range(chaves):
  recebeEntrada= int(input())
  
  for j in range(tabelaTam):
    posicao = (recebeEntrada + j) % tabelaTam
    
    if tabela[posicao] is None:
      tabela[posicao] = recebeEntrada
      break

for i in range(tabelaTam):
  if tabela[i] is not None:
    print(f"{i}: {tabela[i]}")
