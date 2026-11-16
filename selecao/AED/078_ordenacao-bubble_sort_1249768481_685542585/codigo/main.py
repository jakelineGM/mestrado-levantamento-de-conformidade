array = eval(input())

for i in range(1, len(array)):
  for j in range(len(array) - i):
    if array[j] > array[j + 1]:
      print(f"{array[j]} <-> {array[j +1]}")
      array[j], array[j + 1] = array[j + 1], array[j]

print(array)
