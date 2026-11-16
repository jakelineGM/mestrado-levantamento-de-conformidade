#include <stdio.h>

int triangulo_pascal(int linha, int coluna) {
    if (coluna == 0 || coluna == linha)
        return 1;
    return triangulo_pascal(linha - 1, coluna - 1) + triangulo_pascal(linha - 1, coluna);
}

void imprime_tri_pascal(int linhas) {
    for (int i = 0; i < linhas; i++) {
        // Espaços para centralizar
        for (int s = 0; s < linhas - 1 - i; s++)
            printf(" ");
        // Valores da linha
        for (int j = 0; j <= i; j++) {
            printf("%d", triangulo_pascal(i, j));
            if (j < i) printf(" ");
        }
        printf("\n");
    }
}

int main(void) {
    int linhas;
    scanf("%d", &linhas);
    printf("Triangulo de Pascal com %d linhas:\n", linhas);
    imprime_tri_pascal(linhas);
    return 0;
}