def imprime_selection(v):
  tamanho = len(v)
  for i in range(tamanho):
    minimo = i
    
    for j in range(i+1, tamanho):
      if v[j] < v[minimo]:
        minimo = j

    if v[minimo] < v[i]:
      print("{} <-> {}".format(v[i],v[minimo]))
      (v[i], v[minimo]) = (v[minimo], v[i])

lista = eval(input())
imprime_selection(lista)
print(lista)