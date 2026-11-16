def cria_lista_vazia():   
    lista = dict()
    lista['prim'] = None
    lista['fim'] = None
    lista['tamanho'] = 0

    return lista

def imprime(lista):
  aux = lista['prim']
  print(">>", end=" ")
  while aux is not None:
    print(aux['valor'], end=" ")
    aux = aux['prox']
  print()

def insere_fim(lista, valor):
  novo = dict()
  novo['valor'] = valor
  novo['prox'] = None
  if lista['fim'] is not None:
    lista['fim']['prox'] = novo
  else:
    lista['prim'] = novo
  lista['fim'] = novo
  lista['tamanho'] += 1
  return lista
      
   

def remove(lista, valor):  
  while lista['prim'] is not None and lista['prim']['valor'] == valor:
    lista['prim'] = lista['prim']['prox']
    lista['tamanho'] -= 1
  aux = lista['prim']
  if aux is None or aux['prox'] is None:
    lista['fim'] = aux
    
  while aux is not None and aux['prox'] is not None:    
    if aux['prox']['valor'] == valor:
      aux['prox'] = aux['prox']['prox']
      if aux['prox'] is None:
        lista['fim'] = aux           
      lista['tamanho']-=1
    else:
      aux = aux['prox']    
  return lista


def eh_tripla(lista):
  if lista['tamanho'] < 3:
    print("nada")
    return
  contagem = 0
  aux = lista['prim']
  while aux['prox'] is not None and contagem < 2:
      if aux['valor'] == aux['prox']['valor']:
        contagem +=1
      else:
        contagem = 0
      aux = aux['prox']
  if contagem == 2:
    print("tripla")
  else:
    print("nada")

# Programa principal
n = int(input())
for _ in range(n):
  lista = cria_lista_vazia()
  entrada = input().split(' ')
  entrada = [e for e in entrada if len(e) > 0]
  if len(entrada) < 1:
    break
  entrada = list(map(int, entrada))
  remover = entrada.pop()
  for e in entrada:
    insere_fim(lista, e)
  lista = remove(lista, remover)
  #imprime(lista)
  eh_tripla(lista)
  
  