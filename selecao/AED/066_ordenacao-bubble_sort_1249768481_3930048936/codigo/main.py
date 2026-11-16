def bubbleSort(lista):
  tam = len(lista)
  
  for i in range(tam - 1, 0, -1):
    trocou = False
    for j in range(i):
      if lista[j] > lista[j+1]:
        lista[j], lista[j+1] = lista[j+1], lista[j]
        print(lista[j+1],"<->",lista[j])
        trocou = True
    if not trocou:
      return lista
  return lista

lista = eval(input())
print(bubbleSort(lista))