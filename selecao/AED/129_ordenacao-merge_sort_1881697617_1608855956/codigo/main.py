def merge_sort(v):
  n = len(v)
  if n == 1:
    return

  left_array = v[0:n//2]
  right_array = v[n//2:n]

  merge_sort(left_array)
  merge_sort(right_array)
  merge(left_array, right_array, v)

def merge(left_array, right_array, v):
  l = 0
  r = 0
  while l < len(left_array) and r < len(right_array):
    if left_array[l] < right_array[r]:
      v[l+r] = left_array[l]
      l += 1
    else:
      v[l+r] = right_array[r]
      r += 1
  while l < len(left_array):
    v[l+r] = left_array[l]
    l += 1
  while r < len(right_array):
    v[l+r] = right_array[r]
    r += 1


v = eval(input())

while any(v):
  merge_sort(v)
  print(v)
  v = eval(input())
  
