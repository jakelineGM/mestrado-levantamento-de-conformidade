from collections import deque

def brincadeira_com_cartas(N):
    fila = deque(range(1, N + 1))  
    descartadas = []
    
    while len(fila) > 1:
        descartadas.append(fila.popleft())  
        fila.append(fila.popleft())  
    
    
    print(f"Descartadas: {' '.join(map(str, descartadas))}")
 
    print(f"Restou: {fila[0]}")

def main():
    entradas = input()  
    
    
    for N_str in entradas.split():
        N = int(N_str)
        if N == 0:
            break
        brincadeira_com_cartas(N)
        print()

if __name__ == "__main__":
    main()
