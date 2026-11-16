def main():
    from collections import deque
    
    while True:
        entrada = input().split()
        
        for n_str in entrada:
            N = int(n_str)
            if N == 0:
                return
            
            if N == 1:
                print("Descartadas:")
                print("Restou: 1")
                print()
                continue
            
            fila = deque(range(1, N + 1))
            descartadas = []
            
            while len(fila) > 1:
                # Descarta a carta do topo
                descartada = fila.popleft()
                descartadas.append(descartada)
                
                # Coloca a próxima carta no fundo
                if fila:
                    carta_fundo = fila.popleft()
                    fila.append(carta_fundo)
            
            # Imprime resultados
            print(f"Descartadas: {' '.join(map(str, descartadas))}")
            print(f"Restou: {fila[0]}")
            print()

if __name__ == "__main__":
    main()