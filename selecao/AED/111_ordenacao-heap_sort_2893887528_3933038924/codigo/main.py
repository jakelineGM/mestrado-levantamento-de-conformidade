def max_heapfy(i, x):
  if 2*i+2 < len(x) and x[2*i+1] < x[2*i+2] and x[i] < x[2*i+2]:
    x[i], x[2*i+2] = x[2*i+2], x[i]
    max_heapfy(2*i+2, x)
  elif 2*i+1 < len(x) and x[i] < x[2*i+1]:
    x[i], x[2*i+1] = x[2*i+1], x[i]
    max_heapfy(2*i+1, x)

def make_heap(x):
  for i in range(len(x)//2, -1, -1):
    max_heapfy(i, x)

def heap_pop(x):
  x[0], x[len(x) - 1] = x[len(x) - 1], x[0]
  output = x.pop()
  max_heapfy(0, x)
  return output

def heap_sort(x):
  make_heap(x)
  aux = []
  while len(x) > 0:
    aux.insert(0, heap_pop(x))
  return aux

x = eval(input())
while len(x) > 0:
  print(heap_sort(x))
  x = eval(input())