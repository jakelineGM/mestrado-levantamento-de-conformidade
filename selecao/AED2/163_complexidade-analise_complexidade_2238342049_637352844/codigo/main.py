from math import log2

num = int(input())

t_b = 2*(num**2) - 3*num + 1
t_m = 6*num*log2(num) + 8*num - 6

if t_b < t_m:
  print("Usar Bubble Sort")

else:
  print("Usar Merge Sort")