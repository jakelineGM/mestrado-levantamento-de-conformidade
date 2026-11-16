def max_heapify(v, i):
  tam = len(v)
  esq = 2*i + 1
  dir = 2*i + 2
  maior = i
  
  if (esq < tam and v[esq] > v[maior]):
    maior = esq
  if (dir < tam and v[dir] > v[maior]):
    maior = dir

  if (maior != i):
    v[i], v[maior] = v[maior], v[i]
    max_heapify(v, maior)

while True:
  v = eval(input())
  if (len(v) > 0):
    max_heapify(v, 0)
    print(v)
  else:
    break

  