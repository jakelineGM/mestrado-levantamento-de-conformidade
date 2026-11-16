def selectionSort(l):
  for j in range(0, len(l)-1):
    min = j
    for i in range(j+1, len(l)):
      if l[i] < l[min]:
        min = i
    if min != j:
      print(l[j], '<->', l[min])
      l[min], l[j] = l[j], l[min]
  print(l)
l = eval(input())
selectionSort(l)
        