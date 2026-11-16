def max_heapify(v, raiz, tam):
    maior = raiz

    esq = 2 * raiz + 1
    if esq < tam and v[esq] > v[maior]:
        maior = esq

    dir = 2 * raiz + 2
    if dir < tam and v[dir] > v[maior]:
        maior = dir

    if maior != raiz:
        v[raiz], v[maior] = v[maior], v[raiz]
        max_heapify(v, maior, tam)

while True:
    entrada = input()
    if entrada.strip() == "[]":
        break

    vetor = eval(entrada)
    tam = len(vetor)
    if vetor:
        max_heapify(vetor, 0, tam)
    print(vetor)