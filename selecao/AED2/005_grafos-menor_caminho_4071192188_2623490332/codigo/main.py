def buraco_minhoca(planetas):
  if planetas and planetas[-1] == ".":
    planetas.pop()

  indice = {}

  for i, planeta in enumerate(planetas):
    indice[planeta] = i

  total = len(planetas)
  inf = float('inf')

  tempo = [[inf] * total for _ in range(total)]

  for a in range(total):
    tempo[a][a] = 0.0

  while True:
    linha = input()
    campos = linha.split()

    if campos[0] == ".":
      break
      
    saida = campos[0]
    chegada = campos[1]
    desloc = float(campos[2])
    a = indice[saida]
    b = indice[chegada]
    tempo[a][b] = desloc

  for meio in range(total):
    for a in range(total):
      for b in range(total):
        if tempo[a][meio] + tempo[meio][b] < tempo[a][b]:
          tempo[a][b] = tempo [a][meio] + tempo[meio][b]

  volta_tempo = False

  for a in range(total):
    if tempo[a][a] < 0:
      volta_tempo = True
      break

  if volta_tempo:
    print("Great Scott!!")
  else:
    print("Pesado...")

linha = input()
planetas = linha.split()

buraco_minhoca(planetas)