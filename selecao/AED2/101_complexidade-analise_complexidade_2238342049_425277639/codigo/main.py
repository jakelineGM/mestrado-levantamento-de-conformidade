from math import log2

n = int(input())

bub = ((n**2)*2) - 3*n + 1
merg = 6*n*log2(n) + 8*n - 6

if bub > merg:
  print("Usar Merge Sort")
else:
  print("Usar Bubble Sort")