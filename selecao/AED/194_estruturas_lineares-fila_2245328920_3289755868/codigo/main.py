import sys
from collections import deque

def main():
    entrada = sys.stdin.read().strip().split()
    if not entrada:
        return

    duracao_sessao = int(entrada[0])
    tempos_trabalho = list(map(int, entrada[1:]))

    fila_alunos = deque(tempos_trabalho)
    tempo_total = 0

    while fila_alunos:
        tempo_restante = fila_alunos.popleft()
        inicio_da_sessao = tempo_total

        tempo_utilizado = min(tempo_restante, duracao_sessao)
        momento_termino = inicio_da_sessao + tempo_utilizado
        tempo_restante -= tempo_utilizado

        if tempo_restante > 0:
            tempo_total = inicio_da_sessao + duracao_sessao
            fila_alunos.append(tempo_restante)
        else:
            if fila_alunos:
                tempo_total = inicio_da_sessao + duracao_sessao
            else:
                tempo_total = momento_termino
                break

    print(tempo_total)

if __name__ == "__main__":
    main()

