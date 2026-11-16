def max_heapify(values, i, n):
  max_value = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and values[left] > values[max_value]:
    max_value = left

  if right < n and values[right] > values[max_value]:
    max_value = right

  if max_value != i:
    values[i], values[max_value] = values[max_value], values[i]
    max_heapify(values, max_value, n)

def build_max_heap(values):
  n = len(values)
  for i in range (n//2 - 1, -1, -1):
    max_heapify(values, i, n)

def heap_sort(values):
  n = len(values)
  build_max_heap(values)

  for i in range(n-1, 0, -1):
    values[0], values[i] = values[i], values[0]
    max_heapify(values, 0, i)

def clean_input(data:str) -> list:
  values = []
  if data != '[]':
    data = data.strip("[]").split(",")
    values = [int(number.strip()) for number in data]
  return values

while True:
  raw_data = input()
  if raw_data.strip() == '[]':
    break
  values = clean_input(raw_data)
  n = len(values)
  heap_sort(values)
  print(values)