import copy

class Times():
  def __init__(self, times):
    self.times = times

  def busca_time(self, nome_time):
    for t in self.times:
      if(t.nome == nome_time):
        return t

  def __repr__(self):
    for t in self.times:
      print(t)
    return ''

  def hoare(self, lista):
    meio = len(lista)//2
    pivo = lista[meio]
  
    i, j = 0, len(lista)-1
  
    while True:
      while(lista[i] < pivo):
        i += 1
      while(lista[j] > pivo):
        j -= 1
      if(i < j):
        lista[i], lista[j] = lista[j], lista[i]
      else:
        return j
  
  def quick_sort(self, lista):
    nova_lista = copy.copy(lista)
    esq, dir = [], []
    if(len(nova_lista) > 1):
      pc = self.hoare(nova_lista)
      esq = self.quick_sort(nova_lista[:pc])
      dir = self.quick_sort(nova_lista[pc:])
  
      try:
        nova_lista = esq + dir
      except TypeError:
        try:
          nova_lista = esq
        except TyepError:
          nova_lista = dir

    return nova_lista

  def mostra_placar(self):
    self.times = self.quick_sort(self.times)
    
    for t in range(len(self.times)):
      print(f'{t+1} - {self.times[t]}')

class Time():
  def __init__(self, nome):
    self.nome = nome
    self.pontos = 0
    self.vitorias = 0
    self.saldo_gols = 0
    self.n_gols = 0
    self.n_partidas = 0
    self.n_empates = 0
    self.n_derrotas = 0

  def __lt__(self, outro):
    if(self.pontos > outro.pontos):
      return True
    elif((self.pontos == outro.pontos) and (self.vitorias > outro.vitorias)):
      return True
    elif((self.pontos == outro.pontos) and (self.vitorias == outro.vitorias) and (self.saldo_gols > outro.saldo_gols)):
      return True
    elif((self.pontos == outro.pontos) and (self.vitorias == outro.vitorias) and (self.saldo_gols == outro.saldo_gols) and (self.n_gols > outro.n_gols)):
      return True
    elif((self.pontos == outro.pontos) and (self.vitorias == outro.vitorias) and (self.saldo_gols == outro.saldo_gols) and(self.n_gols == outro.n_gols) and (self.n_partidas < outro.n_partidas)):
      return True
    elif((self.pontos == outro.pontos) and (self.vitorias == outro.vitorias) and (self.saldo_gols == outro.saldo_gols) and (self.n_gols == outro.n_gols) and (self.n_partidas == outro.n_partidas) and (self.nome.lower() < outro.nome.lower())):
      return True
    else:
      return False
    
  def __repr__(self):
    return  f'{self.nome}: {self.pontos} pontos, {self.n_partidas} jogos ({self.vitorias}-{self.n_empates}-{self.n_derrotas}), d.g. {self.saldo_gols} ({self.n_gols}-{self.n_gols-self.saldo_gols})'

def processa_jogo(jogo, times):
  res_t1 = jogo.split('#')[0]
  res_t2 = jogo.split('#')[1]

  nome_t1, gols_t1 = res_t1.split(':')
  nome_t2, gols_t2 = res_t2.split(':')
  
  t1 = times.busca_time(nome_t1)
  t2 = times.busca_time(nome_t2)

  t1.n_gols += int(gols_t1)
  t2.n_gols += int(gols_t2)

  t1.saldo_gols += int(gols_t1) - int(gols_t2)
  t2.saldo_gols += int(gols_t2) - int(gols_t1)

  t1.n_partidas += 1
  t2.n_partidas += 1

  empate = gols_t1 == gols_t2
  if not empate:
    vencedor = t1 if int(gols_t1) > int(gols_t2) else t2
    perdedor = t2 if int(gols_t1) > int(gols_t2) else t1
    vencedor.pontos += 3
    vencedor.vitorias += 1
    perdedor.n_derrotas += 1
  else:
    t1.pontos += 1
    t2.pontos += 1
    t1.n_empates += 1
    t2.n_empates += 1

n = eval(input())
campeonatos = []
resultado_campeonatos = []

for i in range(n):
  times, resultado_jogos = [], []
  
  _ = input()
  nome_campeonato = input()
  
  t = int(input())
  for n_times in range(t):
    time = Time(input())
    times.append(time)
  times = Times(times)

  g = int(input())
  for n_jogos in range(g):
    resultado_jogos.append(input())

  for jogo in resultado_jogos:
    processa_jogo(jogo, times)

  campeonatos.append(nome_campeonato)
  resultado_campeonatos.append(times)

for i in range(n):
  print(campeonatos[i])
  resultado_campeonatos[i].mostra_placar()