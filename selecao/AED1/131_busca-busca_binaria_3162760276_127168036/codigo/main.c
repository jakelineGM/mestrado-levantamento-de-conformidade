#include <stdio.h>

// BEGIN

int primeira_ocorrencia(int *v, int size, int chave) {
    int ini = 0, fim = size - 1, resultado = -1;
    while (ini <= fim) {
        int meio = (ini + fim) / 2;
        if (v[meio] == chave) {
            resultado = meio;
            fim = meio - 1;
        } else if (v[meio] < chave) {
            ini = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
    return resultado;
}

int ultima_ocorrencia(int *v, int size, int chave) {
    int ini = 0, fim = size - 1, resultado = -1;
    while (ini <= fim) {
        int meio = (ini + fim) / 2;
        if (v[meio] == chave) {
            resultado = meio;
            ini = meio + 1;
        } else if (v[meio] < chave) {
            ini = meio + 1;
        } else {
            fim = meio - 1;
        }
    }
    return resultado;
}

int buscaBinaria(int *v, int size, int chave) {
    int primeiro = primeira_ocorrencia(v, size, chave);
    if (primeiro == -1)
        return 0;
    int ultimo = ultima_ocorrencia(v, size, chave);
    return primeiro == ultimo;
}

// END

void ler(int *v, int size) {
    for (int i = 0; i < size; i++)
        scanf("%d%*c", &v[i]);
}

int main() {
    int chave;
    int size;
    scanf("%d%*c", &chave);
    scanf("%d%*c", &size);
    int vet[size];
    ler(vet, size);
    if (buscaBinaria(vet, size, chave)) {
        printf("SIM");
    } else {
        printf("NAO");
    }
}
