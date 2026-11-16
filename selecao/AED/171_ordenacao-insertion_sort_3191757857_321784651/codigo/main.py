Entrada = eval(input())

print(Entrada)

i = 1
while i < len(Entrada):
  chave = Entrada[i]
  j = i - 1
  
  while j >= 0 and Entrada[j] > chave:
      if Entrada[j+1] !=  Entrada[j]:
        Entrada[j + 1] = Entrada[j]    
        print(Entrada)
      
      j -= 1
    
  if Entrada[j + 1] != chave:
    Entrada[j + 1] = chave    
    print(Entrada)

  i += 1
  
