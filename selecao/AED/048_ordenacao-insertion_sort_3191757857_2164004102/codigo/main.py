def insertion_sort(l):
  print(l)

  for i in range(1, len(l)):
    key = l[i]
    j = i-1

    while j >= 0 and key < l[j]:
      if(l[j+1] != l[j]):
        l[j+1] = l[j]
        print(l)
      
      j -= 1

    if (l[j+1] != key):
      l[j+1] = key
      print(l)


l = eval(input())

insertion_sort(l)