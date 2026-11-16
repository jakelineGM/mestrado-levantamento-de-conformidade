
tamanho = int(input())
quantidade = int(input())
tabela = [None] * tamanho   

for i in range(quantidade):
  
  valor = int(input())

  cont = 0
  indice = valor % tamanho
  
  while tabela[indice] is not None:
    cont+=1
    indice = (valor + cont)%tamanho
  
  tabela[indice] = valor

for indice in range(tamanho):
  if tabela[indice] is not None:
    print("%d: %d" % (indice, tabela[indice]))
 
  