class Elemento:
  def __init__(self, chave, valor):
    self.chave = chave 
    self.valor = valor

  def __lt__(self, elemento):
    return self.chave < elemento.chave

  def __le__(self, elemento):
    return self.chave <= elemento.chave

  def __ge__(self, elemento):
    return self.chave >= elemento.chave

  def __repr__(self):
    return f"{self.chave} {self.valor}"

def Hoare(lista):
  tam = len(lista)
  if  tam % 2 == 0:
    meio = (tam // 2) - 1
  else:
    meio = (tam // 2)
  pivo = lista[meio]

  i, j = -1, tam

  while True:
    while True:
      i += 1
      if lista[i] >= pivo:
        break
    while True:
      j -= 1
      if lista[j] <= pivo:
        break
    if i < j:
      lista[i], lista[j] = lista[j], lista[i]
    else:
      return j

def QuickSort(lista):

  if len(lista) > 1:
    pontoCorte = Hoare(lista)
    esq = QuickSort(lista[0:pontoCorte+1])
    dir = QuickSort(lista[pontoCorte+1:len(lista)])
    lista = esq + dir
  return lista

casos = eval(input())
numero_caso = 0

while casos != []:
  lista_casos = []
  numero_caso += 1

  for chave, valor in casos:
    lista_casos.append(Elemento(chave,valor))
  lista_ordenada = QuickSort(lista_casos)

  print(f"Caso {numero_caso}")
  for i in lista_ordenada:
    print(i)
  print()
  
  casos = eval(input())
    
  