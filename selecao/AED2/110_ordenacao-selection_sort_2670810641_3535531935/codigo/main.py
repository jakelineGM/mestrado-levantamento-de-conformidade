def imprime_selection(v):
    for i in range(len(v)):
        menor_valor = i
        for j in range(i + 1, len(v)):
            if v[j] < v[menor_valor]:
                menor_valor = j
        if menor_valor != i:
            print(f"{v[i]} <-> {v[menor_valor]}")
            v[i], v[menor_valor] = v[menor_valor], v[i]
        
vetor = eval(input())
imprime_selection(vetor)
print(vetor)