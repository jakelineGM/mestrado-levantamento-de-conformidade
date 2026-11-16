class Grafo:
  def __init__(self):
      self.nomes = []
      self.origens = []
      self.destinos = []
      self.pesos = []

  def adicionar_vertice(self, nome):
      self.nomes.append(nome)

  def indice_do_vertice(self, nome):
      return self.nomes.index(nome)

  def adicionar_aresta(self, origem, destino, peso):
      u = self.indice_do_vertice(origem)
      v = self.indice_do_vertice(destino)
      self.origens.append(u)
      self.destinos.append(v)
      self.pesos.append(peso)

  def tem_ciclo_negativo(self):
      n = len(self.nomes)
      m = len(self.origens)

      dist = [0.0]*n

      for i in range(n-1):
        for j in range(m):
            u = self.origens[j]
            v = self.destinos[j]
            w = self.pesos[j]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

      for j in range(m):
          u = self.origens[j]
          v = self.destinos[j]
          w = self.pesos[j]
          if dist[u] + w < dist[v]:
              return True

      return False

grafo = Grafo()

entrada = input().split()
i = 0
while entrada[i] != ".":
      grafo.adicionar_vertice(entrada[i])
      i +=1

continua_lendo = True
while continua_lendo:
      entrada = input().split()
      origem = entrada[0]
      destino = entrada[1]
      peso = entrada[2]

      if origem == "." and destino == ".":
          continua_lendo = False
      else:
          grafo.adicionar_aresta(origem, destino, float(peso))

if grafo.tem_ciclo_negativo():
    print("Great Scott!!")
else:
    print("Pesado...")

  