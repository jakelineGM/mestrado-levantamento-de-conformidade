def bubble_sort(arr):
  for n in range(len(arr)-1, 0, -1):
    troca = False
    for i in range(n):
      if arr[i] > arr[i + 1]:
        print(f"{arr[i]} <-> {arr[i + 1]}")
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        troca = True
    if not troca:
      break

entrada = eval(input())
bubble_sort(entrada)
print(entrada)