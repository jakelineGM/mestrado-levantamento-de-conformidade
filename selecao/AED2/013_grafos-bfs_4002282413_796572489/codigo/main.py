from collections import deque

N, M, A, L, C = map(int, input().split())

matriz = [list(map(int, input().split())) for _ in range(N)]

fila = deque()
visitado = [[False] * M for _ in range(N)]

# Coloca todas as posições do rio na fila
for i in range(N):
    for j in range(M):
        if matriz[i][j] == 0:
            fila.append((i, j))
            visitado[i][j] = True

# BFS para espalhar a água
while fila:
    x, y = fila.popleft()

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy

        if 0 <= nx < N and 0 <= ny < M and not visitado[nx][ny]:
            if matriz[nx][ny] <= A:
                visitado[nx][ny] = True
                fila.append((nx, ny))

if visitado[L][C]:
    print("Deu ruim!")
else:
    print(":)")