vertices = [nome for nome in input().split() if nome != '.'];
num_vertices = len(vertices)
mapa_vertices = {}

for i in range(len(vertices)):
  nome = vertices[i]
  mapa_vertices[nome] = i;

matriz = []
for i in range(num_vertices):
  matriz.append([float('inf')] * num_vertices);

for i in range(num_vertices):
  matriz[i][i] = 0.0;

while True:
  arestas = input().split()
  if len(arestas) < 3 or arestas[0] == '.':
    break;

  inicio, fim, peso = arestas[0], arestas[1], arestas[2]
  u = mapa_vertices[inicio];
  v = mapa_vertices[fim];
  matriz[u][v] =  eval(peso);

for i in range(num_vertices):
  for j in range(num_vertices):
    for k in range(num_vertices):
      if(matriz[j][i] + matriz[i][k] < matriz[j][k]):
        matriz[j][k] = matriz[j][i] + matriz[i][k];

ciclo_inverso = False;

for i in range(num_vertices):
  if(matriz[i][i] < 0):
    ciclo_inverso = True;
    break;