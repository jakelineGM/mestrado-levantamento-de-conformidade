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

q = int(input())
line = input()
valores = line.split()

fila = cria_fila()
for valor in valores:
  valor = int(valor)
  insere(fila, cria_nodo(valor))

t = 0
while tamanho(fila) > 1:
  nodo = retira(fila)
  nodo['valor'] -= q
  t += q
  if nodo['valor'] > 0:
    insere(fila, cria_nodo(nodo['valor']))
nodo = retira(fila)
t += nodo['valor']
print(t)