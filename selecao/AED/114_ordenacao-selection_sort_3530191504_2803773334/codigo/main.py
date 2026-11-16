def selection_sort(lista):

  for i in range(len(lista) - 1):
    menor = i
    for j in range(i + 1, len(lista)):
      if lista[j] < lista[menor]:
        menor = j

    if i != menor:
      print(f'{lista[i]} <-> {lista[menor]}')
      lista[i], lista[menor] = lista[menor], lista[i]

l = eval(input())

selection_sort(l)
print(l)