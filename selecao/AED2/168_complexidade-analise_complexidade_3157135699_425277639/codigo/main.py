n = int(input())

bub = ((n**2)*2) - 3*n + 1
ins = (((n**2)*3) + 5*n)/2 + 1

if bub > ins:
  print("Usar Insertion Sort")
else:
  print("Usar Bubble Sort")