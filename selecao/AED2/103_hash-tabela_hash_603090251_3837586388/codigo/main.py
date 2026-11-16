#To tentando pegar o codigo p por no colab
tamanhoHash= int(input())
quantidadeNum = int(input())
tabela=[]
cont = 0
while cont < tamanhoHash:
  tabela.append(-1)
  cont+=1
numerosList =[]
for i in range (0, quantidadeNum):
  num = int(input())
  numerosList.append(num)
for i in range(0, quantidadeNum):
  div = numerosList[i] % tamanhoHash
  j = 0
  posicao = (div + j)%tamanhoHash
  while tabela[posicao] != -1:
    j+=1
    posicao=(div+j)%tamanhoHash
  tabela[posicao] = numerosList[i]
aux = 0
while aux < tamanhoHash:
  if tabela[aux] != -1:
    print("%d: %d" % (aux, tabela[aux]))
  aux+=1
