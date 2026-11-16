class Elemento:
  def __init__(self, nome, numero):
    self.nome = nome
    self.numero = numero

entrada = eval(input())
lista_pessoas = []

while entrada != []:
  pessoa = Elemento(entrada[0], entrada[1])
  lista_pessoas.append(pessoa)

  entrada = eval(input())
    
def insertion_sort(balde):
  for i in range(1, len(balde)):
    chave = balde[i]
    j = i - 1

    while j >= 0 and balde[j].numero > chave.numero:
      balde[j + 1] = balde[j]
      j -= 1

    balde[j + 1] = chave

def bucket_sort(lista):
  numeros = [e.numero for e in lista]
  valor_max = max(numeros)
  valor_min = min(numeros)
  baldes = []
  
  n = len(lista)

  for i in range(n):
    baldes.append([])

  for elemento in lista:
    indice = int((elemento.numero - valor_min) / (valor_max - valor_min) * (n-1))
    baldes[indice].append(elemento)

  for balde in baldes:
    insertion_sort(balde)

  lista_ordenada = []

  for balde in baldes:
    lista_ordenada += balde

  return lista_ordenada

pessoas = bucket_sort(lista_pessoas)

for i in pessoas:
  print(f"{i.nome} - {i.numero}")





  
