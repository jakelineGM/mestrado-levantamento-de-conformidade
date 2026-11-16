class Nodo():
  def __init__ (self):
    self.carta = None 
    self.prox = None

class Fila():
  def __init__(self):
    self.tamanho = 0
    self.prim = None
    self.fim = None
  
  def insere(self, carta):
    new_nodo = Nodo()
    new_nodo.carta = carta

    if self.prim is not None:
      new_nodo.prox = self.prim
      self.prim = new_nodo
    else:
      self.prim = new_nodo

    self.tamanho = self.tamanho + 1 

  def retira(self):
    temp = self.prim
    
    if temp is None:
      return None
    if self.tamanho == 1:
      self.tamanho = 0
      carta = self.prim.carta
      self.prim = None
      self.fim = None
      return carta
    elif temp:  
      previous = None
      while temp.prox is not None:
        previous = temp
        temp = temp.prox
      carta = temp.carta
      self.fim = previous
      previous.prox = None
      self.tamanho = self.tamanho - 1
      return  carta
      
  def tamanho():
    return self.tamanho
  
  def imprime(self):
    temp = self.prim

    if temp:  
      while True:
        print(f'carta {temp.carta}')
        if not temp.prox:
          break
        temp = temp.prox


inserir = input().split(' ')
count = 1
for i in inserir:
  if i == '0':
    break
    
  fila = Fila()
  #print(f'Fila: {count}')
  print()
  for x in range(1,int(i)+1):
    fila.insere(x)
  count = count + 1

  #fila.imprime()
  #to_remove = fila.retira()
  #print(f'to remove: {to_remove}')
  
  descartadas = []
  while fila.tamanho > 1:
    #fila.imprime()
    #print()
    to_remove = fila.retira()
    #print(f'to remove: {to_remove}')
    descartadas.append( to_remove )
    fila.insere(fila.fim.carta)
    fila.retira()
    #fila.imprime()
  
  print('Descartadas:', *descartadas)
  print(f'Restou: {fila.prim.carta}')