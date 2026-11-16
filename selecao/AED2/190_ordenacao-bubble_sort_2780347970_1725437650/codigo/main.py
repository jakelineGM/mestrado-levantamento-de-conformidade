def bubble_parcial(lis, K):
  
  lim = 0;
  while(lim!=K):
    i = (len(lis)-1);
    while(i>lim):
      if(lis[i] < lis[i-1]):
        lis[i], lis[i-1] = lis[i-1], lis[i];
      i-=1
    lim +=1;
  return lis;


# Lê uma linhada entrada
entrada = eval(input())

# Enquanto essa linha não contiver a tupla vazia...
while entrada != ():
  # Separa o inteiro K da lista a ser ordenada
  K, lis = entrada
  
  # Chama a função para ordenação parcial
  lis = bubble_parcial(lis, K)
  
  # Imprime a lista parcialmente ordenada
  print(lis)
  
  # Lê a próxima linha da entrada
  entrada = eval(input())