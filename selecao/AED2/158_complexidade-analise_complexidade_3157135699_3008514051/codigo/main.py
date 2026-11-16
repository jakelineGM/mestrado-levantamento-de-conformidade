entrada = int(input())


TempoBubble = 2*(entrada * entrada) - 3 * entrada + 1
TempoInsertion = (3 * (entrada * entrada) + 5 * entrada)/2 + 1

if TempoBubble > TempoInsertion:
  print('Usar Insertion Sort')
else:
  print('Usar Bubble Sort')