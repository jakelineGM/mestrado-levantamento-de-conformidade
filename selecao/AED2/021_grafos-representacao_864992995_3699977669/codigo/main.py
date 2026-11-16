class Grafo:
  def __init__(self, num_vertices):
    self.list_adj = [[] for _ in range(num_vertices)]

  def inserir(self, origem, destino, peso):
    self.remover(origem, destino)

    self.list_adj[origem].append((destino, peso))

    if origem != destino:
      self.list_adj[destino].append((origem, peso))

  def remover(self, origem, destino):
    self._remover(origem, destino)

    if origem != destino:
      self._remover(destino, origem)

  def _remover(self, vertice, target):
    lista = self.list_adj[vertice]
    for i in range(len(lista)):
      vizinho, _ = lista[i]
      if vizinho == target:
        lista.pop(i)
        return
  def peso_aresta(self, origem, destino):
    for (vizinho, peso) in self.list_adj[origem]:
      if vizinho == destino:
        return peso
    return None

num_grafo = 0

num_vertices = int(input())
while num_vertices != 0:
  num_grafo += 1
  print("Grafo", num_grafo)
  
  # Crie um novo grafo
  grafo = Grafo(num_vertices)
  
  # Leia as arestas
  num_arestas = int(input())
  for i in range(num_arestas):
    u, v, w = [int(_) for _ in input().split(',')]
    
    # Insira uma aresta (u, v, w) OU remova a aresta (u, v)
    if w == 0:
      grafo.remover(u, v)
    else:
      grafo.inserir(u, v, w)
    
    
  # Faça as consultas
  num_consultas = int(input())
  for i in range(num_consultas):
    u, v = [int(_) for _ in input().split(',')]
    
    # Consulte a aresta (u, v)
    peso = grafo.peso_aresta(u, v)
    if peso is not None:
      print(f"{u},{v}: {peso}")
    
  # Leia uma linha em branco e descarte; depois leia N para o próximo caso
  # de teste
  input()
  num_vertices = int(input())
  
  # Imprima uma linha em branco
  print()