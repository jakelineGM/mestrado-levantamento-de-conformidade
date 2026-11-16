entrada = eval(input())
maior = entrada[0][1]
menor = entrada[0][1]
trabalho=[]
ordenado=[]

for i in range(0,len(entrada)):
  if entrada[i][1] > maior:
    maior = entrada[i][1]

  if entrada[i][1] < menor:
    menor = entrada[i][1]

maior = maior*10
menor = menor*10

tamanho = (maior-menor)+1
for i in range(0,int(tamanho)):
  trabalho.append([])

for i in range(len(entrada)-1,-1,-1):
  trabalho[int((entrada[i][1]*10)-menor)].append(entrada[i])

for i in range(0,len(trabalho)):
  for j in range(0,len(trabalho[i])):
    if trabalho[i]!=[]:
      ordenado.append(trabalho[i][j])

print(ordenado)

cont = 1
for i in range(len(ordenado)-1,-1,-1):
  ordenado[i][1] = float(ordenado[i][1])
  print(f"{cont}. {ordenado[i][0]} - {ordenado[i][1]}")
  cont=cont+1
    







  

  




  