from collections import deque

class Terminal:
  def __init__(self,q,tempos):
    self.q = q
    self.tempos = deque(tempos)
    self.total_tempo = 0


  def processar(self):
    while self.tempos:
      tempo = self.tempos.popleft()


      if tempo <= self.q:
        self.total_tempo+=self.q
   


      else:
        self.total_tempo += self.q
        self.tempos.append(tempo - self.q)


    if tempo <= self.q:
      self.total_tempo= self.total_tempo - (self.q - tempo)
    return self.total_tempo

q = int(input())
tempos = list(map(int,input().split()))

terminal = Terminal(q,tempos)
resultado = terminal.processar()
print(resultado)
        