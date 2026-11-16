from math import log2

n = int(input())

tempoBubble = 2*(n**2) - 3*n + 1
tempoMerge = 6*n*(log2(n)) + 8*n - 6

if tempoBubble > tempoMerge:
  print("Usar Merge Sort")
else:
  print("Usar Bubble Sort")