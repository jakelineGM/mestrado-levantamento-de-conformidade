def heapify(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)

def heap_sort(L):
    arr = L.copy()
    n = len(arr)
    
    # Constrói max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extrai elementos um por um
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    
    return arr

def main():
    while True:
        entrada = input().strip()
        if entrada == "[]":
            break
        lista = eval(entrada)
        ordenada = heap_sort(lista)
        print(ordenada)

if __name__ == "__main__":
    main()