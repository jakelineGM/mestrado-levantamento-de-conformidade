
import sys

class Time:
  def __init__(self, nome):
    self.nome = nome
    self.pontos = 0
    self.jogos = 0
    self.vitorias = 0
    self.empates = 0
    self.derrotas = 0
    self.gols_marcados = 0
    self.gols_sofridos = 0

  @property
  def saldo_gols(self):
    return self.gols_marcados - self.gols_sofridos

  def atualizar_estatisticas(self, gols_marcados, gols_sofridos):
    self.jogos = self.jogos + 1
    self.gols_marcados = self.gols_marcados + gols_marcados 
    self.gols_sofridos = self.gols_sofridos + gols_sofridos 

    if gols_marcados > gols_sofridos:
      self.vitorias = self.vitorias + 1
      self.pontos = self.pontos + 3
    elif gols_marcados == gols_sofridos:
      self.empates = self.empates + 1
      self.pontos = self.pontos + 1
    else:
      self.derrotas = self.derrotas + 1

  def __str__(self):
    return ( f"{self.nome}: {self.pontos} pontos, {self.jogos} jogos "
             f"({self.vitorias}-{self.empates}-{self.derrotas}), d.g. {self.saldo_gols} "
             f"({self.gols_marcados}-{self.gols_sofridos})"
    )

def comparar_times(time1, time2):
  if time1.pontos != time2.pontos:
    return -1 if time1.pontos > time2.pontos else 1
  if time1.vitorias != time2.vitorias:
    return -1 if time1.vitorias > time2.vitorias else 1
  if time1.saldo_gols != time2.saldo_gols:
    return -1 if time1.saldo_gols > time2.saldo_gols else 1
  if time1.gols_marcados != time2.gols_marcados:
    return -1 if time1.gols_marcados > time2.gols_marcados else 1
  if time1.jogos != time2.jogos:
    return -1 if time1.jogos < time2.jogos else 1

  if time1.nome.lower() != time2.nome.lower():
    return -1 if time1.nome.lower() < time2.nome.lower() else 1
  return 0

def partition(arr, low, high):
    pivot = arr[high]
  
    i = low -1
  
    for j in range(low, high):
      if comparar_times(arr[j], pivot) == -1:
        i = i + 1
        arr[i], arr[j] = arr[j], arr[i]
  
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quick_sort(arr, low, high):
    if low < high:
      pi = partition(arr, low, high)
      quick_sort(arr, low, pi-1)
      quick_sort(arr, pi+1, high)

def processar_campeonato(result):
  
  try:
    separador = input()
    
    nome_campeonato = input()
    if not nome_campeonato:
      return False

    num_times_str = input()
    if not num_times_str:
      return False
      
    num_times = int(num_times_str)
    
  except EOFError:
    return False
  except ValueError:
    return False

  times_nomes = []
  for _ in range(num_times):
    try:
      nome_time = input()
      if not nome_time:
        break
      times_nomes.append(nome_time)
    except EOFError:
      break

  if len(times_nomes) != num_times:
    return True

  mapa_times = {nome_time: Time(nome_time) for nome_time in times_nomes}
  lista_times = list(mapa_times.values())

  try:
    num_jogos_str = input()
    if not num_jogos_str:
      return True
    num_jogos = int(num_jogos_str)
  except EOError:
    return True
  except ValueError:
    return True

  for _ in range(num_jogos):

    try:
      jogo_str = input()
      if not jogo_str:
        break
      
      parte1, parte2 = jogo_str.split('#')

      nome_time1, gols_time1_str = parte1.split(':')
      gols_time1 = int(gols_time1_str)

      nome_time2, gols_time2_str = parte2.split(':')
      gols_time2 = int(gols_time2_str)

      time1 = mapa_times[nome_time1]
      time1.atualizar_estatisticas(gols_time1, gols_time2)

      time2 = mapa_times[nome_time2]
      time2.atualizar_estatisticas(gols_time2, gols_time1)
      
    except EOError:
      break
    except Exception:
      continue
  
  quick_sort(lista_times, 0, len(lista_times)-1)
  #print(nome_campeonato)
  result.append('')
  result.append(nome_campeonato)

  for i, time in enumerate(lista_times):
    #print(f'{i+1} - {time}')
    result.append(f'{i+1} - {time}')
  
  #print()
  
  return i

def main():
  try:
    N_str = sys.stdin.readline().strip()
    if not N_str:
      return
    N = int(N_str)
  except Exception:
    return

  result = []
  for _ in range(N):
    if not processar_campeonato(result):
      break
  for item in result:
    print(item)

main()
