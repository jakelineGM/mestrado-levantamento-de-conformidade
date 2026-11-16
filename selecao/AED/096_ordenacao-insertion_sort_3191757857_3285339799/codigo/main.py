def insertion_sort(vetor):
  print(vetor)
  
  for i in range (1,len(vetor)):
    trocou = False
    chave = vetor[i]
    j = i - 1

    while j >= 0 and vetor[j] > chave:
      vetor[j+1] = vetor[j]
      j -= 1
      trocou = True
      if vetor[j+1]!= vetor[j]:
        print(vetor)

      
    vetor[j+1] = chave
    if trocou:
      print(vetor)

      
    

vetor = eval(input())
insertion_sort(vetor)



      