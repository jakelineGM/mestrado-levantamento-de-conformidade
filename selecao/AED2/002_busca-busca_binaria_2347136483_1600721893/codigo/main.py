def busca_binaria_passos(v, k): 
  passos = []
  inicio = 0
  fim = len(v) - 1

  while inicio <= fim:
    meio = (inicio + fim) // 2
    passos.append(v[meio])

    if v[meio] == k:
      break 
    elif k < v[meio]:
      fim = meio - 1
    else:
      inicio = meio + 1
      
  return passos 

import ast

lista = ast.literal_eval(input()) 
chaves = ast.literal_eval(input()) 


for k in chaves: 
  passos = busca_binaria_passos(lista, k)
  print(passos) 