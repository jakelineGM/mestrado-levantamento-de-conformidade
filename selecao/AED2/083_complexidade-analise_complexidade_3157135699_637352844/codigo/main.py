num = int(input())

t_b = 2*(num**2) - 3*num + 1
t_i = (3*(num**2) + 5*num)/2 + 1

if t_b < t_i:
  print("Usar Bubble Sort")

else:
  print("Usar Insertion Sort")