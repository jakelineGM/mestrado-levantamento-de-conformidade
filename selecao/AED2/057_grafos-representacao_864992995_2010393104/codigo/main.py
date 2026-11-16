num_grafo = 0

num_vertices = int(input())
while num_vertices != 0:
    num_grafo += 1
    print(f"Grafo {num_grafo}")
    
    grafo = []
    for i in range(num_vertices):
        grafo.append([])
    

    num_arestas = int(input())
    for i in range(num_arestas):
        u, v, w = [int(_) for _ in input().split(',')]
        
       
        if w == 0:
            j = 0
            u_encontrado = False
            while j < len(grafo[u]) and u_encontrado is False:
                if grafo[u][j][0] == v:
                    grafo[u].pop(j)
                    u_encontrado = True
                else:
                    j += 1      
            
            j = 0
            v_encontrado = False  
            while j < len(grafo[v]) and v_encontrado is False:
                if grafo[v][j][0] == u:
                    grafo[v].pop(j)
                    v_encontrado = True
                else:
                    j += 1

        else:
            j = 0
            u_encontrado = False
            while j < len(grafo[u]) and u_encontrado is False:
                if grafo[u][j][0] == v:
                    grafo[u][j] = (v, w)
                    u_encontrado = True
                j += 1      

            if u_encontrado is False:
                grafo[u].append((v, w))
            
            j = 0
            v_encontrado = False  
            while j < len(grafo[v]) and v_encontrado is False:
                if grafo[v][j][0] == u:
                    grafo[v][j] = (u, w)
                    v_encontrado = True
                j += 1
                
            if v_encontrado is False:
                grafo[v].append((u, w))
      
    num_consultas = int(input())
    for i in range(num_consultas):
        u, v = [int(_) for _ in input().split(',')]
        
       
        j = 0
        consulta = False
        while j < len(grafo[u]) and consulta is False:
            vizinho = grafo[u][j][0]
            peso = grafo[u][j][1]
            if vizinho == v:
                print(f"{u},{v}: {peso}")
                consulta = True
            j += 1
      
   
    input()
    num_vertices = int(input())
    
    print()