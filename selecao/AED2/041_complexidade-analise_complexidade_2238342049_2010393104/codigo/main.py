from math import log2
def qual_sort(n):
  bubble = (2*(n**2) - (3*n) +1)  
  merge = ((6*n *log2(n)) + 8*n) - 6 

  if bubble > merge:
    escolhido = 'Merge Sort'
  else:
    escolhido = 'Bubble Sort'

  return escolhido


n = eval(input())
print(f'Usar {qual_sort(n)}')