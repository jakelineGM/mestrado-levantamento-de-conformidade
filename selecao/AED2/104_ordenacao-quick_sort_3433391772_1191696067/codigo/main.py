class Elem:
  def __init__(self,chave,valor):
    self.chave = chave
    self.valor = valor

def quick_sort(lis,ini,fim):
  if ini<fim:
    pivo = hoare(lis,ini,fim)
    quick_sort(lis,ini,pivo)
    quick_sort(lis,pivo+1,fim)
    
  
def hoare(lis,inicio,final):
  meio= (inicio+final)//2
  pivo = lis[meio]
  ini = inicio-1
  i=ini
  j=final+1

  while True:
    while True:
      i=i+1
      if lis[i].chave>=pivo.chave:
        break

    while True:
      j=j-1
      if lis[j].chave<=pivo.chave:
        break

    if i>=j:
      return j

    aux = lis[i]
    lis[i]=lis[j]
    lis[j]=aux



entrada = eval(input())
caso = 0
while entrada != []:
  caso = caso+1
  listaTuplas = [Elem(*elem) for elem in entrada]
  quick_sort(listaTuplas,0,len(listaTuplas)-1)

  print("Caso", caso)
  for elem in listaTuplas:
    print(elem.chave,elem.valor)

  entrada = eval(input())
  print("\n")
    
  
  
  
  

  



      
    
    
    
    

