from math import log2

n = int(input('digite o numero n: '))

tb = 2 * (n ** 2) - (3 * n + 1)
tm = ((6 * n) * log2(n)) + (8 * n) - 6 

if tb < tm:
  print('Usar Bubble Sort')
else:
  print('Usar Merge Sort')
