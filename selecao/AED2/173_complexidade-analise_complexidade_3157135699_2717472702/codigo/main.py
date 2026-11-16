n = int(input('digite o numero n: '))

tb = 2 * (n ** 2) - (3 * n + 1)
ti = (3 * (n ** 2) + 5 * n) / 2 + 1

if tb < ti:
  print('Usar Bubble Sort')
else:
  print('Usar Insertion Sort')
