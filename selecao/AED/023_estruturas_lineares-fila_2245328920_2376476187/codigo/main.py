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


def push(fila, valor):
  novo = cria_nodo(valor)

  if fila['prim'] is None:
    fila['prim'] = novo
    fila['fim'] = novo
  else:
    fila['fim']['prox'] = novo
    fila['fim'] = fila['fim']['prox']

  fila['tamanho'] += 1


def pop(fila):
  removido = fila['prim']

  fila['prim'] = fila['prim']['prox']
  fila['tamanho'] -= 1

  removido['prox'] = None
  return removido['valor']


def peek(fila):
  return fila['prim']['valor']


cota = int(input())
tempos = list(map(int, input().split()))

fila = cria_fila()

for tempo in tempos:
  push(fila, tempo)

tempo_total = 0

while fila['tamanho'] > 0:
  tempo = pop(fila)
  
  if tempo <= cota:
    if fila['tamanho'] == 0:
      tempo_total += tempo
    else:
      tempo_total += cota
  else:
    tempo -= cota
    push(fila, tempo)
    tempo_total += cota

print(tempo_total)
