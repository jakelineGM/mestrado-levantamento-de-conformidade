class Elem:
  def __init__(self,chave,valor):
    self.chave = chave
    self.valor = valor

def merge_sort(lis):
  if len(lis)>1:
    meio = (len(lis))//2

    esq = lis[:meio]
    dir = lis[meio:]

    merge_sort(esq)
    merge_sort(dir)

    i=0
    j=0
    k=0

    while i<len(esq) and j<len(dir):  
      if esq[i].chave<dir[j].chave:
        lis[k] = esq[i]
        i=i+1
      elif esq[i].chave>dir[j].chave :
        lis[k]=dir[j]
        j=j+1
      else:
        lis[k]=esq[i] #se as chaves forem iguais, tem q sempre priorizar a esquerda p ficarem em ordem
        i=i+1
      k=k+1   
    
    while i < len(esq):
      lis[k]=esq[i]
      i=i+1
      k=k+1

    while j < len(dir):
      lis[k]=dir[j]
      j=j+1
      k=k+1

entrada = eval(input())
caso = 0
while entrada != []:
  caso = caso+1
  listaTuplas = [Elem(*elem) for elem in entrada]
  merge_sort(listaTuplas)

  print('Caso', caso)
  for elem in listaTuplas:
    print(elem.valor, end='\n')

  entrada = eval(input())
  print()

    



