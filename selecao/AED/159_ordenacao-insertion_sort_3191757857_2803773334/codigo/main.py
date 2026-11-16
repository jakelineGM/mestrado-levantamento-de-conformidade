def insertion_sort(lista):

  print(lista)
  for i in range(len(lista)):
    chave = lista[i]
    j = i - 1

    while j >= 0 and chave < lista[j]:
      
      if lista[j+1] != lista[j]:
        print(lista)
        lista[j+1] = lista[j] 
      j -= 1
      
    if lista[j + 1] != chave:
      print(lista)
    lista[j + 1] = chave

    
l = eval(input())

insertion_sort(l)

print(l)