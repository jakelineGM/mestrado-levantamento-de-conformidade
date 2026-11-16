def qual_sort(n):
  bubble = (2*(n**2) - (3*n) +1)  
  insertion = ((3*(n**2)) + (5*n))/2 + 1  

  if bubble > insertion:
    escolhido = 'Insertion Sort'
  else:
    escolhido = 'Bubble Sort'

  return escolhido


n = eval(input())
print(f'Usar {qual_sort(n)}')