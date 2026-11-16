from collections import deque


def main():
  lista = input().split(' ')
  Q = int(lista[0])
  N = int(lista[1])

  fila = deque()
  for i in range(N):
    lista = input().split(' ')
    nome =  lista[0]
    tempo = int(lista[1])
    fila.append([nome,tempo])

  tot  = 0
  while(fila):
    nome,res = fila.popleft()
    dt = Q if res > Q else res
    tot += dt
    res -= dt

    if(res == 0):
      print(f"{tot} us: {nome} finalizou")
    else:
      fila.append([nome,res])

  print(f"{tot} us: shutdown")
main()
