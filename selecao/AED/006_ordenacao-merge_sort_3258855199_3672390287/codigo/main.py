class ponto:
  def __init__(self, x, y):
    # Construtor.
    # Guarde os atributos self.x e self.y
    self.x = x
    self.y = y
    self.dist = (x**2 + y**2)**(1/2)

  def __lt__(self, outro):
    # Sobrecarga do operador <
    if self.dist != outro.dist:
      if self.dist < outro.dist:
        return True
    else:
      if self.x != outro.x:
        if self.x < outro.x:
          return True
      else:
        if self.y < outro.y:
          return True
        

def intercala(A, B):
  i = 0
  j = 0
  n = len(A) + len(B)
  s = [0]*n
  for k in range (n):
    if i < len(A) and j < len (B):
      if A[i] < B[j]:
        s[k] = A[i]
        i += 1
      else:
        s[k] = B[j]
        j += 1
    else:
      if i >= len(A):
        s[k] = B[j]
        j += 1
      else:
        s[k] = A[i]
        i += 1
  return s


def merge_sort(L):
  if len(L) >=2:
    meio = len(L)//2
    esq = merge_sort(L[0:meio])
    dir = merge_sort(L[meio:len(L)])
    L = intercala(esq, dir)
  return L


# Leitura da entrada
entrada = eval(input())


# Crie uma lista vazia e insira os objetos da classe ponto nela
pontos = []
for item in entrada:
  # processe...
  p = ponto(item[0], item[1])
  pontos.append(p)

# Ordene e imprima de acordo com o enunciado
pontos_ordenados = merge_sort(pontos)

for p in pontos_ordenados:
  print(f"{p.x} {p.y}")