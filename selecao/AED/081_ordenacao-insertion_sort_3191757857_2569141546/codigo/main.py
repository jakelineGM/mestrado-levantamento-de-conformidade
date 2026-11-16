def insertion_sort(entrada):
  print(entrada)
  for i in range(1,len(entrada)):
    num = entrada[i]
    j = i -1
    while j >= 0 and num < entrada[j]:
      if(entrada[j+1] != entrada[j]):
        entrada[j+1] = entrada[j]
        print(entrada)
      j -= 1

    if(entrada[j+1] != num):
      entrada[j+1] = num
      print(entrada)

entrada = eval(input())
insertion_sort(entrada)
