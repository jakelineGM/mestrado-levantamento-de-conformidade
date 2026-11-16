def main():
  linha = input()
  nomes = linha.split()
  if nomes and nomes[-1] == ".":
    nomes.pop()

  arestas = []
  while True:
    linha = input()
    partes = linha.split()
    if partes[0] == ".":
      break 
    origem = partes[0]
    destino = partes[1]
    peso = float(partes[2])
    arestas.append((origem,destino,peso))

  id = {}
  for i, nome in enumerate(nomes):
    id[nome] = i

  arestas_num = []
  for origem, destino, peso in arestas:
    arestas_num.append((id[origem],id[destino],peso))

  n = len(nomes)

  dist = [0.0] * n

  for _ in range(n-1):
    for u,v,p in arestas_num:
      if dist[u] + p < dist[v]:
        dist[v] = dist[u] + p
  tem_ciclo_negativo = False
  for u,v,p in arestas_num:
    if dist[u] + p < dist[v]:
      tem_ciclo_negativo = True
      break 
  if tem_ciclo_negativo:
    print("Great Scott!!")
  else:
    print("Pesado...")

main()