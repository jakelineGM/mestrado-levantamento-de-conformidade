import ast

def insertion(v):
  n = len(v)
  print(v)
  
  for i in range(1, n):
    pivot = v[i];
    j = i-1;
    
    while j >= 0 and v[j] > pivot:    
      aux = v[j+1]
      v[j+1] = v[j]
      if v[j+1] != aux:
        print(v)
      j -= 1

    aux2 = v[j+1]
    v[j+1] = pivot;
    if v[j+1] != aux2: 
      print(v)
        
  return v

valores = ast.literal_eval(input())
insertion(valores)