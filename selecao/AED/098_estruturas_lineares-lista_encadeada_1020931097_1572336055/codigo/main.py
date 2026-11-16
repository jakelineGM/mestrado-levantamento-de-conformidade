import copy 

class No():
  def __init__(self, valor, tempo):
    self.valor = valor
    self.tempo_restante = tempo
    self.prox = None

class LSEC():
  def __init__(self):
    self.prim = No('?', 0)
    self.tamanho = 0

  def add_no(self, no):
    no.prox = self.prim
    if(self.prim.prox is None):
      self.prim.prox = no
      self.tamanho += 1
    else:
      atual = self.prim
      while(atual.prox.valor != '?'):
        atual = atual.prox
      atual.prox = no
      self.tamanho += 1  

  def remove_no(self, no):
    atual = self.prim
    while(atual.prox.valor != no.valor):
      atual = atual.prox
    atual.prox = atual.prox.prox
    self.tamanho -= 1

  def executa_programa(self, cota):
    atual = self.prim.prox
    tempo_decorrido = 0
    while(self.tamanho != 0):
      atual = atual if atual.valor != '?' else atual.prox
      tempo_exec = cota if cota < atual.tempo_restante else atual.tempo_restante
      tempo_decorrido += tempo_exec
      atual.tempo_restante -= tempo_exec
      if(atual.tempo_restante == 0):
        prox = atual.prox
        self.remove_no(copy.copy(atual))
        print(f"{tempo_decorrido} us: {atual.valor} finalizou")
        atual = prox
      else:
        atual = atual.prox
    print(f"{tempo_decorrido} us: shutdown")
      
  def __repr__(self):
    lista = []
    atual = self.prim.prox
    while(atual.valor != '?'):
      lista.append(atual.valor + '#' + str(atual.tempo_restante))
      atual = atual.prox      
    return ', '.join(lista)

# Lê as configurações do exercício
cota, num_programas = map(int, input().split(' '))

# Cria uma lista ligada vazia
lista = LSEC()

# Lê os programas e os insere na lista
for _ in range(num_programas):
  nome, tempo_total_string = input().split(' ')
  programa = No(nome, int(tempo_total_string))
  lista.add_no(programa)

lista.executa_programa(cota)


# Agora é com você! Simule a execução de todos os programas, manipulando corretamente
# a lista circular e imprimindo sempre que um programa finaliza sua execução