class Elem:
  def __init__(self, chave, valor):
    self.chave = chave
    self.valor = valor

  def __lt__(lesq, ldir):
    return lesq.chave < ldir.chave

  def __repr__(self):
    return str(self.valor)

def hoare(lista):
  meio = (len(lista)-1)//2
  pivo = lista[meio]
  i = -1
  j = len(lista) 
  while True:
    i = i + 1
    while lista[i].chave < pivo.chave:
      i = i + 1
    
    j = j - 1
    while lista[j].chave > pivo.chave:
      j = j - 1
    
    if i < j:
      lista[i], lista[j] = lista[j], lista[i]
    else:
      return j

entrada = eval(input())
caso = 1
while entrada != []:
  lis = []
  
  for chave, valor in entrada:
    lis.append(Elem(chave, valor))

  pontoCorte = hoare(lis)
  
  print(f"Caso {caso}")
  print("esq: ")
  
  for i in range(0, pontoCorte + 1):
    print(f"{lis[i]}")

  print("dir: ")
  
  for j in range(pontoCorte + 1, len(lis)):
    print(f"{lis[j]}")

  entrada = eval(input())
  caso = caso + 1
