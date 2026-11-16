class Nodo:
  def __init__(self, carta):
    self.carta = carta
    self.prox = None

class Fila:
  def __init__(self):
    self.prim = None
    self.fim = None
    self.tamanho = 0

def insere(fila, carta):
  novo = Nodo(carta)
  if fila.fim:
    fila.fim.prox = novo
  fila.fim = novo
  if not fila.prim:
    fila.prim = novo
  fila.tamanho += 1

def retira(fila):
  if fila.prim is None:
    return None
  carta = fila.prim.carta
  fila.prim = fila.prim.prox
  if fila.prim is None:
    fila.fim = None
  fila.tamanho -= 1
  return carta

Ns = list(map(int, input().split()))

for N in Ns:
  if N == 0:
    break

  fila = Fila()
  for i in range(1, N+1):
    insere(fila, i)

  descartadas = []
  while fila.tamanho > 1:
    descartadas.append(retira(fila))
    insere(fila, retira(fila))
  carta_restante = retira(fila)

  print("Descartadas:", ' '.join(map(str, descartadas)))
  print("Restou:", carta_restante)
  print()