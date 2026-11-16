def busca_binaria(lis,chave):
  ini = 0
  fim = len(lis)-1

  verificados = []

  while ini <= fim:
    meio = (ini+fim) // 2
    verificados.append(lis[meio])

    if lis[meio] == chave:
      break 
    if lis[meio] < chave:
      ini = meio + 1
    else:
      fim = meio - 1
      
  return verificados

lis = eval(input())
chaves = eval(input())

for k in chaves:
  print(busca_binaria(lis,k))