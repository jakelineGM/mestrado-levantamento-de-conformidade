from collections import deque

entradas = list(map(int, input().split()))

for N in entradas:
  if N == 0:
    break

  fila = deque(range(1,N+1))
  descartadas = []

  while len(fila) > 1:
    descartadas.append(fila.popleft())
    fila.append(fila.popleft())

  print("Descartadas:", " ".join(map(str,descartadas)))
  print("Restou: ", fila[0])