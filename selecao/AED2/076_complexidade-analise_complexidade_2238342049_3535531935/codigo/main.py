from math import log2

n = int(input())

t_b = 2*n**2 - 3*n + 1
t_m = 6*n*log2(n) + 8*n - 6

if t_b < t_m:
  print("Usar Bubble Sort")
else:
  print("Usar Merge Sort")