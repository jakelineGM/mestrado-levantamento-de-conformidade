from math import log2

def bubble(x):
  primeiraParte= 2*(x**2) 
  segundaParte=(3*x) 

  resultado = primeiraParte - segundaParte + 1
  return resultado
  
def merge(x):
  parteUm= 6*x*log2(x)
  parteDois= 8*x
  result= (parteUm + parteDois)-6
  return result


x=eval(input())
b=bubble(x)
m=merge(x)

if(b>m):
  print("Usar Merge Sort")
else:
  print("Usar Bubble Sort")
  