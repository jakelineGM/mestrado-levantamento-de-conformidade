def bubble_parcial(lis, K):
  num = len(lis)
  for i in range(K):
    for j in range((num-1), 0, -1):
      if(lis[j] < lis[j-1]):
        aux = lis[j]
        lis[j] = lis[j-1]
        lis[j-1] = aux

# Lê uma linhada entrada
entrada = eval(input())

# Enquanto essa linha não contiver a tupla vazia...
while entrada != ():
  # Separa o inteiro K da lista a ser ordenada
  K, lis = entrada
  
  # Chama a função para ordenação parcial
  bubble_parcial(lis, K)
  
  # Imprime a lista parcialmente ordenada
  print(lis)
  
  # Lê a próxima linha da entrada
  entrada = eval(input())