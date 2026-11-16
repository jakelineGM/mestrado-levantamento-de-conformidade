def a(v):
  n = len(v)
  for i in range(n-1):
    min_index = i
    for j in range(i+1, n):

      if v[j] <v[min_index]:
        min_index=j

    if min_index != i:
      print(f"{v[i]} <-> {v[min_index]}")

      v[i], v[min_index] = v[min_index], v[i]
        
            




  
try:
  entrada = input()
  if entrada:
    lista = eval(entrada)
    a(lista)
    print(lista)
    
except (SyntaxError, NameError):
  pass