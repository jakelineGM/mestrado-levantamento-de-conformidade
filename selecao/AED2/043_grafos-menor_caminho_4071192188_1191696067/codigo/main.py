
planetas = input().split()
inf = float('inf')
matriz = []
flag = False
for i in range(0,len(planetas)-1):
  matriz.append([])
  for j in range(0,len(planetas)-1):
    if i == j:
      matriz[i].append(0)
    else:
      matriz[i].append(inf)

entrada = input()
while entrada != '. . 0':
  vetorentrada = entrada.split()
  linha = planetas.index(vetorentrada[0])
  coluna = planetas.index(vetorentrada[1])
  matriz[linha][coluna] = float(vetorentrada[2])
  vetorentrada.clear()
  entrada = input()

for k in range(0, len(planetas)-1):
  for i in range(0, len(planetas)-1):
    for j in range(0, len(planetas)-1):
      if matriz[i][k]!= inf and matriz[k][j]!=inf:
        if float(matriz[i][k])+float(matriz[k][j])<float(matriz[i][j]):
          matriz[i][j] = float(matriz[i][k])+float(matriz[k][j])

for i in range(0,len(planetas)-1):
  if matriz[i][i]<0:
    flag = True

if flag==True:
  print("Great Scott!!")
else:
  print("Pesado...")
    
  