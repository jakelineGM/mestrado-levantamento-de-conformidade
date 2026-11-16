def max_heapify(v, i):
  max = i
  left = 2*i + 1
  right = 2*i + 2

  if left < len(v) and v[left] > v[i]:
    max = left

  if right < len(v) and v[right] > v[max]:
    max = right

  if max != i:
    aux = v[i]
    v[i] = v[max]
    v[max] = aux
    max_heapify(v, max)


v = eval(input())
while any(v):
  max_heapify(v, 0)
  print(v)
  v = eval(input())