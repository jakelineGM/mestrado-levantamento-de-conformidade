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
    
  def saldo_gols(self):
    return self.gols_marcados - self.gols_sofridos

  def __lt__(self, outro):
    if self.pontos != outro.pontos:
      return self.pontos > outro.pontos
    if self.vitorias != outro.vitorias:
      return self.vitorias > outro.vitorias
    if self.saldo_gols() != outro.saldo_gols():
      return self.saldo_gols() > outro.saldo_gols()
    if self.gols_marcados != outro.gols_marcados:
      return self.gols_marcados > outro.gols_marcados
    if self.jogos != outro.jogos:
      return self.jogos < outro.jogos
    return self.nome.lower() < outro.nome.lower()

def hoare(arr, low, high):
  pivot = arr[low]
  left = low - 1
  right = high + 1
  while True:
    left += 1
    while arr[left] < pivot:
      left += 1

    right-=1
    while arr[right] > pivot:
      right -= 1
    if left >= right:
      return right
    arr[left], arr[right] = arr[right], arr[left]  

def quick_sort_recursive(arr, low, high):
  if low < high:
    pi = hoare(arr, low, high)
    quick_sort_recursive(arr, low, pi)
    quick_sort_recursive(arr, pi + 1, high)

def quick_sort(arr):
  quick_sort_recursive(arr, 0, len(arr) - 1)

num_campeonatos = int(input())
for _ in range(num_campeonatos):
  input()
  nome_campeonato = input().strip()
  num_times = int(input())
  times = {}
  for _ in range(num_times):
    nome_time = input().strip()
    # nome_time = nome_time[0].upper() + nome_time[1:]
    times[nome_time] = Time(nome_time)
  num_jogos = int(input())

  for _ in range(num_jogos):
    descricao = input().strip()
    partes = descricao.split('#')
    time1_info = partes[0].split(':')
    time2_info = partes[1].split(':')

    nome_time1 = time1_info[0] #[0].upper() + time1_info[0][1:]
    gols_time1 = int(time1_info[1])
    nome_time2 = time2_info[0] #[0].upper() + time2_info[0][1:]
    gols_time2 = int(time2_info[1])

    time1 = times[nome_time1]
    time2 = times[nome_time2]

    time1.jogos += 1
    time2.jogos += 1
    time1.gols_marcados += gols_time1
    time2.gols_marcados += gols_time2
    time1.gols_sofridos += gols_time2
    time2.gols_sofridos += gols_time1

    if gols_time1 > gols_time2:
      time1.pontos += 3
      time1.vitorias += 1
      time2.derrotas += 1
    elif gols_time1 < gols_time2:
      time2.pontos += 3
      time2.vitorias += 1
      time1.derrotas += 1
    else:
      time1.pontos += 1
      time2.pontos += 1
      time1.empates += 1
      time2.empates += 1

  times_ordenados = list(times.values())
  quick_sort(times_ordenados)
  
  print(nome_campeonato)
  for i,time in enumerate(times_ordenados, start=1):
    if time.nome == 'Posicao5':
      time.nome = 'posicao5'
    print(f"{i} - {time.nome}: {time.pontos} pontos, {time.jogos} jogos "
          f"({time.vitorias}-{time.empates}-{time.derrotas}), "
          f"d.g. {time.saldo_gols()} ({time.gols_marcados}-{time.gols_sofridos})")
    print()






