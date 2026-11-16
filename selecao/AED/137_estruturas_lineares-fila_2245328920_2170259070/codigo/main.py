class Nodo:
  def __init__(self, tempo):
    self.tempo = tempo
    self.prox = None

class Fila:
  def __init__(self):
    self.prim = None
    self.fim = None
    self.tamanho = 0

  def insere(self, tempo):
    novo = Nodo(tempo)
    if self.tamanho == 0:
      self.prim = novo
      self.fim = novo
    else:
      self.fim.prox = novo
      self.fim = novo
    self.tamanho += 1
  def retira(self):
    if self.tamanho == 0:
      return None
    removido = self.prim 
    valor = removido.tempo
    self.prim = removido.prox
    
    if self.prim is None:
      self.fim = None

      
    self.tamanho -= 1
    return valor

Q = int(input().strip())

linha = input().strip()
if linha == "":
  tempos = []
else:
  tempos = list(map(int, linha.split()))

fila = Fila()
for t in tempos:
  fila.insere(t)

tempo_total = 0 
while fila.tamanho > 0:
  t = fila.retira()
  if t <= Q:
    
    if fila.tamanho == 0:
      tempo_total += t
    else:
      tempo_total += Q
  else: 
    tempo_total += Q
    resto = t - Q
    fila.insere(resto)

print(tempo_total)
    
      
    

    