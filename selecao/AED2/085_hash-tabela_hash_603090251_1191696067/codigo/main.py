tam = int(input())
nvalores = int(input())
tabela = []

for i in range(0,tam):
  tabela.append(None)

cont=0
while cont<nvalores:
  entrada = int(input())
  agaka = int(entrada%tam)
  
  if tabela[agaka] is None:
    tabela[agaka] = entrada
    
  else:
    i = 1
    agalinha = int((agaka+i)%tam)
    while tabela[agalinha] is not None:
      i = i+1   
      agalinha = int((agaka+i)%tam)
      
    tabela[agalinha] = entrada
  cont = cont+1

for i in range(0,len(tabela)):
  if(tabela[i]is not None):
    print(f"{i}: {tabela[i]}")

  
      
