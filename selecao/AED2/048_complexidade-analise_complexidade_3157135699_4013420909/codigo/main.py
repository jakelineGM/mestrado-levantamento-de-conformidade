entradaN = int(input())

tempoBubble = (2 * (entradaN ** 2)) - (3 * entradaN) + 1

tempoInsetion = (((3 * (entradaN ** 2)) + (5 * entradaN)) // 2) + 1

if tempoBubble > tempoInsetion:
  print("Usar Insertion Sort")
else: 
  print("Usar Bubble Sort")