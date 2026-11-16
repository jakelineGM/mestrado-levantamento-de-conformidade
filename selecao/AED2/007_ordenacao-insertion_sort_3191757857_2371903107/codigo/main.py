def insertion_sort(lista):
  print(lista)
  length = len(lista)
  
  for i in range(length-1):
    prox = lista[i+1]
    j = i
    troca = False
    
    while lista[j] > prox and j >= 0:

      if lista[j] != lista[j+1]:
        lista[j+1] = lista[j]
        print(lista)
      j -= 1
      troca = True
      
    lista[j+1] = prox
    if troca: print(lista)


lista = eval(input())
insertion_sort(lista)