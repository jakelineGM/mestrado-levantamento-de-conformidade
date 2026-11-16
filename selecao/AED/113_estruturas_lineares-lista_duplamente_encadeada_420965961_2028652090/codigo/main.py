def cria_nodo(valor):
  nodo = dict()

  nodo['valor'] = valor
  nodo['prox'] = None

  return nodo

def cria_fila():
  fila = dict()

  fila['prim'] = None
  fila['fim'] = None
  fila['tamanho'] = 0

  return fila

def insere(fila, novo):
  if fila['prim'] is None:
    fila['prim'] = novo

  if fila['fim'] is None:
    fila['fim'] = novo
  else:
    fila['fim']['prox'] = novo
    fila['fim'] = novo
  fila['tamanho'] += 1

def retira(fila):
  fila['tamanho'] -= 1

  nodo = fila['prim']

  if nodo is not None:
    fila['prim'] = nodo['prox']

  return nodo

def tamanho(fila):
  return fila['tamanho']

line = input()
valores = line.split()

for valor in valores:
  valor = int(valor)
  if valor == 0:
    break
  fila = cria_fila()
  for i in range(1, valor + 1):
    insere(fila, cria_nodo(i))

  d = []
  while tamanho(fila) > 1:
    nodo = retira(fila)
    d.append(str(nodo['valor']))
    nodo = retira(fila)
    insere(fila, cria_nodo(nodo['valor']))

  print('Descartadas: ', ' '.join(d))
  nodo = retira(fila)
  print('Restou: ', nodo['valor'])