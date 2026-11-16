def max_heapfy(lista, j):
  tamanho = len(lista)
  i = j
  if (2*i + 2) < tamanho:  
    if lista[i] < lista[2*i  + 1] or lista[i] < lista[2*i + 2]:
      if lista[2*i + 1] >= lista[2*i + 2]:
        aux = lista[i]
        lista[i] = lista[2*i + 1]
        lista[2*i + 1] = aux
        i += 1
      else:
        aux = lista[i]
        lista[i] = lista[2*i + 2]
        lista[2*i + 2] = aux
        i += 1
    else:
      i += 1
    max_heapfy(lista, i) 
  if (2*i + 1) < tamanho:   
    if lista[i] < lista[2*i  + 1]:
      aux = lista[i]
      lista[i] = lista[2*i + 1]
      lista[2*i + 1] = aux
  return lista


def le_varias_listas():
  import ast
  while True:
    lista = ast.literal_eval(input())
    if lista == []:
      break
    max_heapfy(lista, 0)
    print(lista)

    
le_varias_listas()
  