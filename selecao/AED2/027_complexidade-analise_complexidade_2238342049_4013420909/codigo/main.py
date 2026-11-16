from math import log2

entrada = int(input())

tempoBublbeSort = (2 * (entrada**2)) - (3*entrada) + 1

tempoMergeSort = (6*entrada) * log2(entrada) + (8*entrada) - 6

if tempoBublbeSort < tempoMergeSort:
  print("Usar Bubble Sort")
else:
  print("Usar Merge Sort")