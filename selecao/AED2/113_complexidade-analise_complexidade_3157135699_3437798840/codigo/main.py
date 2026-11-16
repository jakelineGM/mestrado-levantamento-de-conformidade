
def bubble(x):
  primeiraParte= 2*(x**2) 
  segundaParte=(3*x) 

  resultado = primeiraParte - segundaParte + 1
  return resultado
  
def inse(x):
  parteUm= 3*(x**2)
  parteDois= 5*x
  result= (parteUm + parteDois)/2 +1
  return result
  
x=eval(input())

b=bubble(x)
i=inse(x)

if(b>i):
  print("Usar Insertion Sort")
else:
  print("Usar Bubble Sort")
  