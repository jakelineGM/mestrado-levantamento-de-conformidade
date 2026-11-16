class Elem:
  def __init__(self,chave,valor):
    self.chave = chave
    self.valor = valor

def hoare(lis):
  esq = []
  dir = []
  meio = ((len(lis)-1))//2
  pivo = lis[meio]
  ini = -1
  final = len(lis)
  i=ini
  j=final

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
      esq.extend(lis[:j+1])
      dir.extend(lis[j+1:])
      return esq, dir

    aux=lis[i]
    lis[i]=lis[j]
    lis[j]=aux
    

entrada = eval(input())
caso = 0
while entrada != []:
  caso = caso + 1
  listaTuplas = [Elem(*elem) for elem in entrada]
  esq,dir = hoare(listaTuplas)
  
  print("Caso",caso)
  print("esq:", end=" ")
  for elem in esq:
    print(elem.valor, end=" ")
  print("\ndir:", end=" ")
  for elem in dir:
    print(elem.valor, end=" ")
  print("\n")
  
  entrada = eval(input())
  