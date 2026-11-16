def imprime_selection(v):
  n = len(v)
  for i in range(n-1):
    mi = i
    for j in range (i+1,n):
      if v[j] < v[mi]:
        mi = j

    if mi != i:
      print(f"{v[i]} <-> {v[mi]}")
      v[i], v[mi] = v[mi], v[i]
  print(v)

entrada = input(" ")
numeros = eval(entrada)

imprime_selection(numeros)