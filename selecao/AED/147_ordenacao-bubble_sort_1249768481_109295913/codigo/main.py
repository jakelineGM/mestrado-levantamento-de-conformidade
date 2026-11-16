def imprime_bubble(v):
  # Tamanho da lista
  list_lenght = len(v)
  
  # Percorre a lista inteira
  for i in range(list_lenght):
    #Analisa os itens adjacentes)
    for j in range(list_lenght - i-1):
     if(v[j]>v[j+1]):
      #Mostra  a troca
      print(f"{v[j]} <-> {v[j+1]}")
      # Realiza a troca com uma variavel
      temp=v[j]
      v[j]=v[j+1]
      v[j+1]=temp
  #Mostra a lista ordenada
  print(v)
  
#Entrada dos dados
entry = eval(input())
imprime_bubble(entry)

