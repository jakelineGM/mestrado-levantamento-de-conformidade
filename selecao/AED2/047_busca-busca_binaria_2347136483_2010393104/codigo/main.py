def busca_binaria(lis, k):
  esq = 0
  dir = len(lis) - 1
  passagem = []
  
  while esq<=dir :
   meio = (esq+dir)//2
   passagem.append(lis[meio])
    
   if lis[meio] == k:
     return passagem 
   elif lis[meio] < k:
     esq = meio +1
   else:
     dir = meio - 1
    
  return passagem  

lis = eval(input())
chave = eval(input())

for i in range(len(chave)):
  print(busca_binaria(lis, chave[i]))