from math import log2 

entrada = int(input())


TempoBubble = 2*(entrada * entrada) - 3 * entrada + 1
TempoMerge = 6 * entrada * log2(entrada) + 8 * entrada - 6

if TempoBubble > TempoMerge:
  print('Usar Merge Sort')
else:
  print('Usar Bubble Sort')