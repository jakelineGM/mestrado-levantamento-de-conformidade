from collections import deque

def main():
  Q = int(input().strip())
  linha = input().strip()
  if not linha:
    print(0)
    return

  tempos = list(map(int, linha.split()))

  fila = deque(tempos)
  tempo_total = 0

  while fila:
    t_aluno = fila.popleft()
    if not fila:
      if t_aluno <= Q:
        tempo_total += t_aluno
        breakpoint
      else:
        tempo_total += Q
        fila.append(t_aluno - Q)

    else:
      if t_aluno > Q:
        tempo_total += Q
        fila.append(t_aluno - Q)
      else:
        tempo_total += Q

  print(tempo_total)

main()