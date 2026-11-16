import sys
from collections import deque

def main():
  numeros = list(map(int, sys.stdin.read().split()))

  primeiro_caso = True

  for n in numeros:
    if n == 0:
      break
    fila = deque(range(1, n + 1))
    descartadas = []

    while len(fila) > 1:
      descartadas.append(fila.popleft())
      fila.append(fila.popleft())

    if not primeiro_caso:
      print()
    primeiro_caso = False

    if descartadas:
      print("Descartadas: " + " ".join(str(x) for x in descartadas))
    else:
      print("Descartadas:")

    print(f"Restou: {fila[0]}")

if __name__ == "__main__":
  main()