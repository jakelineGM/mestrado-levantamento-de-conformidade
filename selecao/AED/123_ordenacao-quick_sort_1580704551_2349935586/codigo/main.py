# Classe para armazenar as estatísticas
class Team:
  def __init__(self, name):
    self.name = name
    self.points = 0
    self.games_played = 0
    self.wins = 0
    self.draws = 0
    self.losses = 0
    self.goals_for = 0
    self.goals_against = 0

  @property
  def goal_difference(self):
    # Retorna o saldo de gols
    return self.goals_for - self.goals_against

# Lógica de ordenação
def is_better(a, b):

  # Mais pontos
  if a.points != b.points:
    return a.points > b.points

  # Mais vitórias
  if a.wins != b.wins:
    return a.wins > b.wins

  # Saldo de gols
  if a.goal_difference != b.goal_difference:
    return a.goal_difference > b.goal_difference

  # Mais gols marcados
  if a.goals_for != b.goals_for:
    return a.goals_for > b.goals_for
  
  # Menos partidas jogadas
  if a.games_played != b.games_played:
    return a.games_played < b.games_played

  # Ordem lexicográfica
  return a.name.lower() < b.name.lower()

# Quick Sort
def quick_sort(L, start=0, end=None):

  if end is None:
    end = len(L)-1
    
  if start < end:
    p = partition(L, start, end)
    quick_sort(L, start, p-1)
    quick_sort(L, p+1, end)

def partition(L, start, end):
  # Seleciona o último elemento como pivot
  pivot = L[end]
  i = start

  for j in range(start, end):
    if is_better(L[j], pivot):
      L[j], L[i] = L[i], L[j] # troca
      i += 1
  # Coloca o pivot no local correto
  L[i], L[end] = L[end], L[i]
  return i

# Lógica principal
def solve():

  # Lista para armazenar os resultados dos campeonatos
  championship_results = []
  
  try:
    # Lê o número de campeonatos
    n = int(input())

    for i in range(n):
      # Lê e descarta a linha em branco
      input()

      # Lê o nome do campeonato
      champ_name = input()

      # Lê o número de times e cria o dicionário de estatísticas
      t = int(input())
      teams_stats = {}

      for _ in range(t):
        team_name = input()
        teams_stats[team_name] = Team(team_name)

      # Lê o número de jogos
      g = int(input())

      for _ in range(g):

        # Processa cada jogo
        game_str = input()

        part1, part2 = game_str.split("#")
        name1, goals1_str = part1.split(":")
        name2, goals2_str = part2.split(":")

        goals1 = int(goals1_str)
        goals2 = int(goals2_str)

        # Pega os objetos dos times
        team1 = teams_stats[name1]
        team2 = teams_stats[name2]

        # Atualiza estatísticas gerais
        team1.games_played += 1
        team2.games_played += 1
        team1.goals_for += goals1
        team2.goals_for += goals2
        team1.goals_against += goals2
        team2.goals_against += goals1

        # Atualiza pontos, vitórias, derrotas e empates
        if goals1 > goals2: # Time 1 venceu
          team1.points += 3
          team1.wins += 1
          team2.losses += 1
        elif goals2 > goals1: # Time 2 venceu
          team2.points += 3
          team2.wins += 1
          team1.losses += 1
        else: # Empate
          team1.points += 1
          team2.points += 1
          team1.draws += 1
          team2.draws += 1

      # Todos os jogos processados
      # Criar lista e ordenar
      team_list = list(teams_stats.values())
      quick_sort(team_list, 0, len(team_list) - 1)

      # Armazena o resultado
      championship_results.append((champ_name, team_list))

    # Imprimir saída formatada
    num_champs = len(championship_results)
    #print()
    for i, (champ_name, sorted_team_list) in enumerate(championship_results):
    
      print(champ_name)
      for rank, team in enumerate(sorted_team_list, 1):
        print(f"{rank} - {team.name}: {team.points} pontos, {team.games_played} jogos "
              f"({team.wins}-{team.draws}-{team.losses}), "
              f"d.g. {team.goal_difference} ({team.goals_for}-{team.goals_against})")

        if i < num_champs - 1:
          print()

  except EOFError:
    pass # Fim da entrada

# Executa a solução
if __name__ == "__main__":
  solve()    