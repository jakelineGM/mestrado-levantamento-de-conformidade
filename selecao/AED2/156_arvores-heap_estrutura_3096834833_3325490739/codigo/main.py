def max_heap(a,i,n):
  maior = i
  esq = 2*i+1
  dir = 2*i+2

  if esq < n and a[esq] > a[maior]:
    maior = esq

  if dir < n and a[dir] > a[maior]:
    maior = dir

  if maior != i:
    a[i],a[maior] = a[maior],a[i]
    max_heap(a,maior,n)
    
while True:
  start = eval(input())
  if start == []:
    break
  
  max_heap(start,0,len(start))
  print(start)
