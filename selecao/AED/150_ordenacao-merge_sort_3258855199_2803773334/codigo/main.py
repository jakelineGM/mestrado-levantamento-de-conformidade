class Ponto:
  def __init__(self, x, y):
    self.x = x
    self.y = y
    self.distancia = (x**2 + y**2) ** 0.5

  def __lt__(self, outro):
    if self.distancia != outro.distancia:
      return self.distancia < outro.distancia

    if self.x != outro.x:
      return self.x < outro.x

    return self.y < outro.y

def mergesort(lista):
  if len(lista) <= 1:
    return lista

  meio = len(lista) // 2
  esq = mergesort(lista[:meio])
  dir = mergesort(lista[meio:])

  return merge(esq, dir)

def merge(esq, dir):
  ordenado = []

  i = 0
  j = 0

  while i < len(esq) and j < len(dir):
    if esq[i] < dir[j]:
      ordenado.append(esq[i])
      i += 1

    else:
      ordenado.append(dir[j])
      j += 1

  ordenado.extend(esq[i:])
  ordenado.extend(dir[j:])

  return ordenado

entrada = eval(input())
pontos = [Ponto(x,y) for x, y in entrada]

pontos_ordenados = mergesort(pontos)
for ponto in pontos_ordenados:
  print(ponto.x, ponto.y)
    