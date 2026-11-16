valores = []
bucket = []
saida = []

entrada = eval(input())
while entrada != []:
  valores.append(entrada)
  entrada = eval(input())

maior = valores[0][1]
menor = valores[0][1]

for i in range(0, len(valores)):
  if valores[i][1]>maior:
    maior = valores[i][1]
  if valores[i][1]<menor:
    menor = valores[i][1]

for i in range(0,4):
  bucket.append([])

for i in range(0,len(valores)):
  indice = int((valores[i][1] * len(bucket))//(maior+1))
  bucket[indice].append(valores[i])

for i in range(0,len(bucket)):
  #vi esse comando no stackOverFlow para ordenar baseando so no segundo 
  #elemento da tupla, que é o que importa aq
  bucket[i].sort(key=lambda tup: tup[1])

for i in bucket:
  for j in i:
    saida.append(j)

for i in range(0,len(saida)):
  print(f"{saida[i][0]} - {saida[i][1]}")


