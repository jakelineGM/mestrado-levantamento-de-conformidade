def selection_sort(entrada):
  for i in range(len(entrada)):
    min = i
    for j in range(i + 1, len(entrada)):
      if(entrada[j] < entrada[min]):
        min = j

    if(i != min):
      print("{entrada[i]} <-> {entrada[min]}")
      entrada[i], entrada[min] = entrada[min], entrada[i]
          
entrada = eval(input())

selection_sort(entrada)
print(entrada)