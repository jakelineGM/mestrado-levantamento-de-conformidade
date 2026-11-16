passosN = int(input())
Tb = (2*(passosN * passosN) - 3*passosN +1)

Ti = (((3*(passosN*passosN) + 5*passosN)/2)+1)

if Tb>Ti:
  print("Usar Insertion Sort")
else:
  print("Usar Bubble Sort")