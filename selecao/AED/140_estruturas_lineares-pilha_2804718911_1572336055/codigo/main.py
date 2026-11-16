import copy 

class No():
  def __init__(self, valor):
    self.valor = valor
    self.prox = None

class Pilha():
  def __init__(self):
    self.topo = None
    self.tamanho = 0
    self.continua = True
    self.saida = ''

  def push(self, no):
    no.prox = self.topo
    self.topo = no
    self.tamanho += 1
    self.saida += f'push {no.valor}\n'

    if(no.valor == 0):
      self.continua = False

  def pop(self):
    if(self.tamanho > 0):
      no = self.topo
      self.topo = no.prox
      self.tamanho -= 1
      self.saida += f'pop {no.valor}\n'
      return no

  def peek(self):
    if self.topo is not None:
      return self.topo

  def computa(self):
    if(self.tamanho >= 2):
      try:
        n_pop1 = pilha.pop()
        n_pop2 = pilha.pop()
        
        result = n_pop1.valor + n_pop2.valor
        pilha.push(No(result))
        if(self.peek().valor < 0 and self.tamanho == 1):
          self.continua = False
          return
        elif(self.peek().valor < 0 and self.tamanho > 1):
          self.computa()
      except AttributeError:
        self.continua = False
        pass
    else:
      self.continua = False

  def get_tamanho(self):
    return self.tamanho

# Programa principal
pilha = Pilha()

try:
  while(pilha.continua):
    valor = int(input())
    no = No(valor)
    pilha.push(no)
    if(no.valor < 0):
      pilha.computa()
  
except ValueError:
  pass
print(pilha.saida)