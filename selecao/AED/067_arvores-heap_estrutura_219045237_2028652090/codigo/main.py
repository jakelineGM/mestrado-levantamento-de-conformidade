def max_heapify(lista, root = 0):
  m = root

  l = 2 * root + 1
  if l < len(lista) and lista[l] > lista[m]:
    m = l

  r = 2 * root + 2
  if r < len(lista) and lista[r] > lista[m]:
    m = r

  if m != root:
    lista[m], lista[root] = lista[root], lista[m]
    max_heapify(lista, m)


v = eval(input())
while len(v) > 0:
  max_heapify(v)
  print(v)
  v = eval(input())
