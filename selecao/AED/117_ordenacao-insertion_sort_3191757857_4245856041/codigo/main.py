def insertion_sort(lista):
  print(lista)
  aux = lista.copy()
  for i in range(1, len(lista)):
    chave = lista[i]
    j = i - 1

    #mod = False
    while j >= 0 and lista[j] > chave:
      lista[j+1] = lista[j]
      j -= 1
      # print('lista', lista, 'aux', aux)
      if lista != aux:
        print(lista)
        aux = lista.copy()
    
    if lista[j+1] != chave:
      lista[j+1] = chave
      print(lista)

lista_input = input()
lista = eval(lista_input)

insertion_sort(lista)