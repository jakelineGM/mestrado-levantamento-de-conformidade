class ponto:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def dist(self):
    return (self.x**2 + self.y**2)**0.5

  def __le__(self, outro):
    if self.dist() == outro.dist():
      if self.x == outro.x:
        return self.y <= outro.y
      else:
        return self.x <= outro.x
    else:
      return self.dist() <= outro.dist()
  
  def __str__(self):
    return f'{self.x} {self.y}'

def merge_sort(A):
  
  if len(A)<=1:
    return A
    
  met_esq = A[:len(A)//2]
  met_dir = A[len(A)//2:]
    
  met_esq = merge_sort(met_esq)
  met_dir = merge_sort(met_dir) 

  return merge(met_esq,met_dir)


def merge(esq,dir):
  A = []
  i = j = 0

  while i < len(esq) and j < len(dir):
    if esq[i] <= dir[j]:
      A.append(esq[i])
      i+=1
    else:
      A.append(dir[j])
      j+=1

  while i < len(esq):
    A.append(esq[i])
    i+=1
    
  while j < len(dir):
    A.append(dir[j])
    j+=1
  return A

# Leitura da entrada
entrada = eval(input())


# Crie uma lista vazia e insira os objetos da classe ponto nela
pontos = []
for item in entrada:
  pontos.append(ponto(*item))

pontos = merge_sort(pontos)

for item in pontos:
  print(item)
# Ordene e imprima de acordo com o enunciado