n = int(input())

t_b = 2*n**2 - 3*n + 1
t_i = (3*n**2 + 5*n)/2 + 1

if t_b < t_i:
  print("Usar Bubble Sort")
else:
  print("Usar Insertion Sort")