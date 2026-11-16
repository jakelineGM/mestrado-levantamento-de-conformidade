import ast
import math

class ponto:
  def __init__(self, x, y):
    # Construtor.
    # Guarde os atributos self.x e self.y
    self.x = x
    self.y = y
    # raiz da distância ao quadrado à origem
    self._dist = math.sqrt((x * x) + (y * y))

  def __lt__(self, outro):
    # Sobrecarga do operador <
    # menor distância primeiro
    if self._dist != outro._dist:
      return self._dist < outro._dist

    # empate: menor x primeiro
    if self.x != outro.x:
      return self.x < outro.x

    # empate: menor y primeiro
    return self.y < outro.y

def merge(left, right):
  """
  Intercala duas listas já ordenadas usando apenas '<'
  """
  res = []
  i = j = 0
  while i < len(left) and j < len(right):
    if not (right[j] < left[i]):
      res.append(left[i])
      i += 1
    else:
      res.append(right[j])
      j += 1

  res.extend(left[i:])
  res.extend(right[j:])
  return res

def merge_sort(L):
  """
  Merge sort agnóstico ao tipo (usa apenas <)
  """
  if len(L) <= 1:
    return L
  mid = len(L) // 2
  left = merge_sort(L[:mid])
  right = merge_sort(L[mid:])
  return merge(left, right)


if __name__ == "__main__":
  # Leitura da entrada
  entrada = input().strip()
  tuplas = ast.literal_eval(entrada)
  
  # Crie uma lista vazia e insira os objetos da classe ponto nela
  pontos = [ponto(x, y) for (x, y) in tuplas]
  pontos_ordenados = merge_sort(pontos)

  for p in pontos_ordenados:
    print(p.x, p.y)