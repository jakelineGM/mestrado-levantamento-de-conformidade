def filhos(i):
  return i*2 + 1, i*2 + 2

def max_heapify(A, idx = 0):
  f1, f2 = filhos(idx)
  if f1 >= len(A):
    return
  if f2 >= len(A):
    if A[idx] < A[f1]:
      aux = A[idx]
      A[idx] = A[f1]
      A[f1] = aux
      max_heapify(A, f1)
  else:
    f = None
    if A[f1] >= A[f2]:
      f = f1
    else:
      f = f2
    if A[idx] < A[f]:
      aux = A[idx]
      A[idx] = A[f]
      A[f] = aux
      max_heapify(A, f)


while (l := eval(input())) != []:
  max_heapify(l)
  print(l)
