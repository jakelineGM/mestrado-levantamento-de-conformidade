def Intercalacao(vetorA, vetorB):
  tamA = len(vetorA)
  tamB = len(vetorB)

  vetorC = []
  k = 0
  f = 0
  while k < tamA and f < tamB:
    if(vetorA[k] < vetorB[f]):
      vetorC.append(vetorA[k])
      k += 1
    else:
      vetorC.append(vetorB[f])
      f += 1

  while k < tamA:
    vetorC.append(vetorA[k])
    k += 1

  while f < tamB:
    vetorC.append(vetorB[f])
    f += 1
    
  return vetorC

  
vetorA = eval(input())
vetorB = eval(input())
vetorC = Intercalacao(vetorA, vetorB)

print(vetorC)