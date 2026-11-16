def bubblesort(l, n):
  i = 0
  while i < n-1:
    j = 0
    troca = False
    while j < n - i - 1:
      if l[j] > l[j+1]:
        print(l[j], ' <-> ', l[j+1])
        l[j], l[j+1] = l[j+1], l[j]
        troca = True
      j += 1
    i += 1
    if not troca:
      i=n
  return l

l = eval(input())
l = bubblesort(l,len(l))
print(l)