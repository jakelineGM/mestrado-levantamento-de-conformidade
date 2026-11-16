num_grafo = 0

num_vertices = int(input())
while num_vertices != 0:
  num_grafo += 1
  print("Grafo", num_grafo)
  
  # Crie um novo grafo

  grafo = [{}for _ in range(num_vertices)]
  
  # Leia as arestas
  num_arestas = int(input())
  for i in range(num_arestas):
    u, v, w = [int(_) for _ in input().split(',')]
    
    # Insira uma aresta (u, v, w) OU remova a aresta (u, v)

    if w == 0:
      grafo[u].pop(v, None) #remove v da lista de u, pulando se nao existir
      grafo[v].pop(u, None) #remove u da lista de v, pulando se nao existir
    else:
      grafo[u][v] = w #grafo nao direcionado, adiciona a aretsa nas duas direcoes
      grafo[v][u] = w
      
  # Faça as consultas
  num_consultas = int(input())
  for i in range(num_consultas):
    u, v = [int(_) for _ in input().split(',')]
    
    # Consulte a aresta (u, v)
    
    if v in grafo[u]:
      print(f"{u},{v}: {grafo[u][v]}")
    
  # Leia uma linha em branco e descarte; depois leia N para o próximo caso
  # de teste
  input()
  num_vertices = int(input())
  
  # Imprima uma linha em branco
  print()