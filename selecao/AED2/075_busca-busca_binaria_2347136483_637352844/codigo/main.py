lista_entrada = eval(input())
lista_chaves = eval(input())

def busca_binaria(lista, chave):
  inicio = 0
  fim = len(lista) - 1
  caminho = []
  
  while inicio <= fim:
    meio = (inicio + fim)//2

    caminho.append(lista[meio])

    if chave == lista[meio]:
      return caminho
    elif chave < lista[meio]:
      fim = meio - 1
    else:
      inicio = meio + 1

  return caminho

for i in lista_chaves:
  lis = busca_binaria(lista_entrada, i)
  print(lis)