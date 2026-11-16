def hoare(L, prim, ult):
  pivo = L[prim]
  i = prim - 1
  j = ult + 1

  while True:
    i+=1
    while L[i]<pivo:
      i+=1
    j-=1
    while L[j]>pivo:
      j-=1
    if i>=j:
      return j
    L[i],L[j] = L[j],L[i]

def quick_sort(L,prim, ult):
  if prim < ult:
    p = hoare(L, prim, ult)
    quick_sort(L,prim,p)
    quick_sort(L,p+1,ult)


A = eval(input())
while A!=[]:
  quick_sort(A, 0, len(A)-1)
  print(A)
  A = eval(input()) 
  
    