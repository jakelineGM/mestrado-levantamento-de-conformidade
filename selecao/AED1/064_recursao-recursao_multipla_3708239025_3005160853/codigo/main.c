#include <stdio.h>

int pascal(int linha, int coluna) {
    if (coluna == 0 || coluna == linha)
        return 1;

    return pascal(linha - 1, coluna - 1) + pascal(linha - 1, coluna);
}

void imprimirEspacos(int n) {
    if (n <= 0) return;
    printf(" ");
    imprimirEspacos(n - 1);
}

void imprimirLinha(int col, int linha) {
    if (col > linha) return;

    printf("%d", pascal(linha, col));

    if (col < linha)
        printf(" ");

    imprimirLinha(col + 1, linha);
}

void imprimirTriangulo(int n, int atual) {
    if (atual == n) return;

    imprimirEspacos(n - atual - 1);
    imprimirLinha(0, atual);
    printf("\n");

    imprimirTriangulo(n, atual + 1);
}

int main() {
    int n;
    scanf("%d", &n);

    printf("Triangulo de Pascal com %d linhas:\n", n);
    imprimirTriangulo(n, 0);

    return 0;
}