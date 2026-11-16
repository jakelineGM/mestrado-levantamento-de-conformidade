Q = int(input())
entrada_alunos = input().split()
fila = []
for tempo in entrada_alunos:
  fila.append(int(tempo))
tempo_total = 0
while len(fila) > 0:
  tempo_necessario = fila.pop(0)
  if tempo_necessario > Q:
    tempo_total = tempo_total + Q
    sobra = tempo_necessario - Q
    fila.append(sobra)
  else:
    if len(fila) > 0:
      tempo_total = tempo_total + Q
    else:
      tempo_total = tempo_total + tempo_necessario

print(tempo_total)