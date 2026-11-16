def selectionsort(l, n):
  i = 0
  while i < n - 1:
    idx_menor = i
    j = i + 1
    while j < n:
      if l[j] < l[idx_menor]:
        idx_menor = j
      j += 1
    if l[idx_menor] != l[i]:
      print(l[i], '<->', l[idx_menor])
      l[i], l[idx_menor] = l[idx_menor], l[i]
    i += 1
  print(l)

l = eval(input())
l = selectionsort(l, len(l))
    