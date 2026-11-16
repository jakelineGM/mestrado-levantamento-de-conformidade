def imprime_lista(l):
  print(l)

def insertionSort(l):
  imprime_lista(l)
  subLi = len(l)
#l = lista
#subLi = sublista
  
  for i in range(1, subLi):
    chave = l[i]
    j = i - 1

    while(j >= 0 and l[j] > chave):
      if(l[j + 1] != l[j]):
        l[j + 1] = l[j]
        imprime_lista(l)
      else:
        l[j + 1] = l[j]
      j -= 1
      
    if(l[j + 1] != chave):
      l[j + 1] = chave
      imprime_lista(l)

entrada = eval(input())
insertionSort(entrada)