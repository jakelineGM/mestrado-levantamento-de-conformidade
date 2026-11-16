def bubble_sort(v):
  tamanho = len(v)
  for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
      if v[j] > v[j + 1]:
        print(f"{v[j]} <-> {v[j + 1]}")
        v[j], v[j + 1] = v[j + 1], v[j]
  print(v) 

entrada = input()
lista = eval(entrada)
bubble_sort(lista)