class ponto:
  def __init__(self, x, y):
    # Construtor.
    # Guarde os atributos self.x e self.y

    self.x  = x
    self.y = y
    self.dist2 = x*x + y*y

  def __lt__(self, outro):
    # Sobrecarga do operador <
    # 
    if self.dist2 != outro.dist2:
      return self.dist2 < outro.dist2
    if self.x != outro.x:
      return self.x < outro.x
    return self.y < outro.y

def merge_sort(lista):
  n = len(lista)

  if n<=1:
    return lista[:]

  meio = n//2
  esquerda = merge_sort(lista[:meio])
  direita = merge_sort(lista[meio:])


  i = j = 0

  resultado = []

  while i < len(esquerda) and j < len(direita):
    if esquerda[i] < direita[j]:
      resultado.append(esquerda[i])
      i = i+1
    else:
      resultado.append(direita[j])
      j = j+1

  resultado.extend(esquerda[i:])
  resultado.extend(direita[j:])
  return resultado





  


# Leitura da entrada
entrada = eval(input())


# Crie uma lista vazia e insira os objetos da classe ponto nela
pontos = []
for (x,y) in entrada:
  pontos.append(ponto(x,y))

pontos_ordenados = merge_sort(pontos)

for p in pontos_ordenados:
  print(p.x, p.y)
  # processe...


# Ordene e imprima de acordo com o enunciado