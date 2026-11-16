def merge(array, p, q, r):
  left = array[p:q + 1]
  right = array[q + 1:r + 1]

  i, j = 0, 0
  k = p

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      array[k] = left[i]
      i = i + 1
    else:
      array[k] = right[j]
      j = j + 1

    k = k + 1

  while i < len(left):
    array[k] = left[i]
    i = i + 1
    k = k + 1

  while j < len(right):
    array[k] = right[j]
    j = j + 1
    k = k + 1

def merge_sort(array, p, r):
  if p >= r:
    return

  q = (p + r) // 2
  merge_sort(array, p, q)
  merge_sort(array, q + 1, r)
  merge(array, p, q, r)


arrays = [[]]

while True:
  array = eval(input())

  if not array:
    break

  arrays.append(array)
  
del arrays[0]

for i in arrays:
  merge_sort(i, 0, len(i) - 1)
  print(i)
