def busca_binaria(v, chave):
    esq = 0
    dir = len(v) - 1
    elementos = []
    while esq <= dir:
        med = (esq + dir) // 2
        elementos.append(v[med])
        
        if v[med] > chave:
            dir = med - 1
        elif v[med] < chave:
            esq = med + 1
        else:
            esq = dir + 1
    return elementos

lista_ordenada = eval(input())
lista_de_chaves = eval(input())

for i in lista_de_chaves:
    print(busca_binaria(lista_ordenada, i))