def imprime_selection(v):
  n = len(v)
  for i in range(n-1):
    min_index = i
    for j in range(i + 1, n):
      if v[j] < v[min_index]:
        min_index = j

    if min_index != i:
      print(f"{v[i]} <-> {v[min_index]}")
      v[i], v[min_index] = v[min_index], v[i]

entrada = input().strip()
v = eval(entrada)
imprime_selection(v)
print(v)