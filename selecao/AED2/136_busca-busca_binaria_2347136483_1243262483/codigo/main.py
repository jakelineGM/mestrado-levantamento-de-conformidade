def busca_binaria_trace(v, k):
    esq, dir = 0, len(v) - 1
    verificados = []

    while esq <= dir:
        meio = (esq + dir) // 2
        verificados.append(v[meio])

        if v[meio] == k:
            return verificados
        elif v[meio] < k:
            esq = meio + 1
        else:
            dir = meio - 1

    return verificados


# programa principal
v = eval(input().strip())
chaves = eval(input().strip())

for k in chaves:
    print(busca_binaria_trace(v, k))