class Par:
  def __init__(self, chave, valor):
    self.valor = valor
    self.chave = chave

  def __lt__(self, outro):
    return self.chave < outro.chave

  def __le__(self, outro):
    return self.chave <= outro.chave

def merge(esq, dir):
  resultado_mer = []
  i = j = 0
  esq_dois = len(esq)
  dir_dois = len(dir)

# Dei ctrl da questão anterior
  while(i < esq_dois and j < dir_dois):
    if(esq[i] <= dir[j]):
      resultado_mer.append(esq[i])
      i += 1
    else:
      resultado_mer.append(dir[j])
      j += 1
  while(i < esq_dois):
    resultado_mer.append(esq[i])
    i += 1
  while(j < dir_dois):
    resultado_mer.append(dir[j])
    j += 1

  return resultado_mer

def merge_sort(L):
  if(len(L) <= 1):
    return L
    
  meio = len(L) // 2
  esq = merge_sort(L[:meio])
  dir = merge_sort(L[meio:])
  return merge(esq, dir)
  
caso = 1
entrada = eval(input())

while(entrada != []):
  Pares = [Par(chave, valor) for chave, valor in entrada]
  Pares_ordenados = merge_sort(Pares)

  print(f"Caso {caso}")
  for par in Pares_ordenados:
    print(par.valor)
  print()
  caso += 1
  entrada = eval(input())