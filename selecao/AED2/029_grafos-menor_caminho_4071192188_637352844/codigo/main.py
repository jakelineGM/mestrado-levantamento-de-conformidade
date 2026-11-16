import sys

def main():
  data = sys.stdin.read().split()
  idx = 0

  names = []
  while data[idx] != '.':
    names.append(data[idx])
    idx += 1
  idx += 1

  n = len(names)
  index = {name: i for i, name in enumerate(names)}

  INF = float('inf')
  dist = [[INF] * n for _ in range(n)]
  for i in range(n):
    dist[i][i] = 0

  while True:
    a, b, w = data[idx], data[idx + 1], data[idx + 2]
    idx += 3
    if a == '.' and b == '.' and w == '0':
      break
    i, j = index[a], index[b]
    dist[i][j] = float(w)

  for k in range(n):
    for i in range(n):
      if dist[i][k] == INF:
        continue
      dik = dist[i][k]
      for j in range(n):
        if dik + dist[k][j] < dist[i][j]:
          dist[i][j] = dik + dist[k][j]

  if any(dist[i][i] < 0 for i in range(n)):
    print("Great Scott!!")
  else:
    print("Pesado...")

main()