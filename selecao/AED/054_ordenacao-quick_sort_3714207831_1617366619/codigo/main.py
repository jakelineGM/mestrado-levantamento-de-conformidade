from math import ceil

def hoare(l):
  size = len(l)
  meio = ceil(size/2)
  pivot = l[meio]

  i = 0
  j = size - 1
  
  while True:
    while l[i] < pivot:
      i += 1
    while l[j] > pivot:
      j -= 1
    if i < j:
      l[i], l[j] = l[j], l[i]
    else:
      return j

def quicksort(l):
  if len(l) > 1:
    pontoCorte = hoare(l)
    esq = quicksort(l[:pontoCorte])
    dir = quicksort(l[pontoCorte:])
    l = esq + dir
  return l

l = eval(input())
while l != []:
  print(quicksort(l))
  l = eval(input())