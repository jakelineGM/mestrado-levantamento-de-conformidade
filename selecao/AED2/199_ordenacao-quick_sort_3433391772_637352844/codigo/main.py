class Elem:
  def __init__(self, chave, valor):
    self.chave = chave
    self.valor = valor

  def __lt__(self, outro):
    return self.chave < outro.chave

  def __gt__(self, outro):
    return self.chave > outro.chave

def hoare(lista):
  i = 0
  j = len(lista) - 1

  if len(lista) % 2 != 0:
    pivo = lista[len(lista)//2]
  else:
    pivo = lista[len(lista)//2 - 1]

  while True:
    while lista[i] < pivo:
      i += 1
    while lista[j] > pivo:
      j -= 1

    if i >= j:
      return j

    lista[i], lista[j] = lista[j], lista[i]
    i += 1
    j -= 1

def quick_sort(lista):
  if len(lista) <= 1:
    return lista

  pivo = hoare(lista)
  esquerda = quick_sort(lista[:pivo + 1])
  direita = quick_sort(lista[pivo + 1:])

  return esquerda + direita

entrada = eval(input())
k = 0

while entrada != []:
  k += 1
  lista_elementos = []
  
  for item in entrada:
    e = Elem(item[0], item[1])
    lista_elementos.append(e)

  lista_ordenada = quick_sort(lista_elementos)
  print(f"Caso {k}")
  
  for elem in lista_ordenada:
    print(f"{elem.chave} {elem.valor}")

  print()
  
  entrada = eval(input())
    
