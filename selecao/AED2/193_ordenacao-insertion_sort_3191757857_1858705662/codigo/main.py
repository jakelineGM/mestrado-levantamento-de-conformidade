entrada = input()
valores = eval(entrada)

def imprime_insertion(lista):
  print(lista[:])

  for i in range(1, len(lista)):
    chave = lista[i]
    j = i -1

    while j >= 0 and lista[j] > chave:
      if lista[j+1] != lista[j]:
        lista[j+1] = lista[j]
        print(lista)
      else:
        lista[j+1] = lista[j]

      j-=1

    if lista[j+1] != chave:
      lista[j+1] = chave
      print(lista[:])

imprime_insertion(valores)

    