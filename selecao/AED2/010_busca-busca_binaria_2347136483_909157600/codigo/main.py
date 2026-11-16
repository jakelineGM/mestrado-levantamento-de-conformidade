def busca_binaria(lis, inicio, fim, chave, lis_verificados):
  if inicio > fim:
    return lis_verificados
  
  meio = (inicio + fim)//2
  lis_verificados.append(lis[meio])
  
  if lis[meio] == chave:
    return lis_verificados

  if lis[meio] > chave:
    return busca_binaria(lis, inicio, meio-1, chave, lis_verificados)
  else:
    return busca_binaria(lis, meio+1, fim, chave, lis_verificados)
  


lis = eval(input())
chaves = eval(input())

for i in range(len(chaves)):
  lis_verificados = busca_binaria(lis, 0, len(lis)-1, chaves[i], [])
  print(lis_verificados)


