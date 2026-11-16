def calculo_tempo_terminal():
  Q = int(input())

  tempos = list(map(int, input().split()))

  tempo_total = 0
  fila = tempos[:]

  while fila:
    atual = fila.pop(0)
    if atual <= Q:
      if len(fila) == 0:
        tempo_total += atual
      else:
        tempo_total += Q
    else:
      tempo_total += Q
      fila.append(atual - Q)

  print(tempo_total)

calculo_tempo_terminal()