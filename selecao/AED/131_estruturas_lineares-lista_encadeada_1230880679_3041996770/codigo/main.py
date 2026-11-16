N = int(input())

for _ in range(N):
  dados = list(map(int, input().split()))

  lista = []
  i = 0
  while dados[i] != 0:
    lista.append(dados[i])
    i += 1

  remover = dados[i+1]

  lista = [x for x in lista if x != remover]

  encontrou = False
  if len(lista) >= 3:
    cont = 1
    for i in range(1, len(lista)):
      if lista[i] == lista[i-1]:
        cont +=1
        if cont >= 3:
          encontrou = True
          break
      else:
        cont = 1
  if encontrou:
    print("tripla")
  else:
    print("nada")
    
  
          
        
        
      
      
    
  
    
  