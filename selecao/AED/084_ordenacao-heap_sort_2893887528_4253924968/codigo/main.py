def max_heapfy(A, n, i):
  largest = i
  left = 2*i + 1
  right = 2*i + 2

  if left < n and A[left] > A[largest]:
    largest = left
  if right < n and A[right] > A[largest]:
    largest = right
  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    max_heapfy(A, n, largest)

def build_max_heap(A):
  n = len(A)
  for i in range(n//2 -1, -1, -1):
    max_heapfy(A,n,i)

def heap_sort(L):
  n = len(L)
  build_max_heap(L)
  for i in range(n-1, 0, -1):
    L[0], L[i] = L[i], L[0]
    max_heapfy(L, i, 0)

while True:
  s = input().strip()
  if not s:
    continue
  if s == "[]":
    break
  L = eval(s)
  if isinstance(L, list) and len(L) > 1:
    heap_sort(L)
  print(L)