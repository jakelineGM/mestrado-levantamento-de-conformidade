num_grafo = 0

num_vertices = int(input())
while num_vertices != 0:
  num_grafo += 1
  print("Grafo", num_grafo)
  
  # Crie um novo grafo
  grafo = [[] for _ in range(num_vertices)]
  
  # Leia as arestas
  num_arestas = int(input())
  for i in range(num_arestas):
    u, v, w = [int(_) for _ in input().split(',')]
    
    # Insira uma aresta (u, v, w) OU remova a aresta (u, v)
    if w == 0:
      
        for a in grafo[u]:
          if a[0] == v:
            grafo[u].remove(a)
            
        for a in grafo[v]:
          if a[0] == u:
            grafo[v].remove(a)
    else:
      grafo[u].append((v,w))
      grafo[v].append((u,w))
    
  
    
  # Faça as consultas
  num_consultas = int(input())
  for i in range(num_consultas):
    u, v = [int(_) for _ in input().split(',')]
    
    # Consulte a aresta (u, v)
    for aresta in grafo[u]:
      if aresta[0] == v:
        print(f"{u},{v}: {aresta[1]}")
        break
    
  # Leia uma linha em branco e descarte; depois leia N para o próximo caso
  # de teste
  input()
  num_vertices = int(input())
  
  # Imprima uma linha em branco
  print()