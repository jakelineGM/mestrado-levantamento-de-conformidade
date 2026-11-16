n = int(input())

tempoBubble = 2*(n**2) - 3*n + 1
tempoInsertion = ((3*(n**2) + 5*n)/2) + 1

if tempoBubble > tempoInsertion:
  print("Usar Insertion Sort")
else:
  print("Usar Bubble Sort")