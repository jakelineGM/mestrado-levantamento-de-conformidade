from collections import deque

def main():
    Q = int(input())
    tempos = list(map(int, input().split()))
    
    fila = deque(tempos)
    tempo_total = 0
    
    while fila:
        aluno = fila.popleft()
        
        if aluno <= Q:
            # Aluno termina nesta sessão
            # Mas sessão dura Q minutos se houver outros esperando
            if fila:
                tempo_total += Q  # Sessão completa (tem outros)
            else:
                tempo_total += aluno  # Último, só precisa do que usa
        else:
            # Aluno não termina
            tempo_total += Q  # Usa sessão completa
            aluno -= Q
            
            # Volta para fila
            fila.append(aluno)
    
    print(tempo_total)

if __name__ == "__main__":
    main()