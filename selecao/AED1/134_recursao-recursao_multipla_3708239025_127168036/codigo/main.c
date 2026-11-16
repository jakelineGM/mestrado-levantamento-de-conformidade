#include <stdio.h>

// Função recursiva para calcular o valor na posição (linha, coluna)
int pascal(int linha, int coluna) {
    if (coluna == 0 || coluna == linha) {
        return 1;
    }
    return pascal(linha - 1, coluna - 1) + pascal(linha - 1, coluna);
}

// Função para imprimir o triângulo de Pascal com n linhas
void imprimeTriangulo(int n) {
    for (int i = 0; i < n; i++) {
        // Imprime espaços para alinhar à esquerda
        for (int j = 0; j < n - i - 1; j++) {
            printf(" ");
        }
        // Imprime os números da linha i
        for (int j = 0; j <= i; j++) {
            printf("%d", pascal(i, j));
            if (j < i) {
                printf(" ");  // apenas entre os números, não após o último
            }
        }
        printf("\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);
    printf("Triangulo de Pascal com %d linhas:\n", n);
    imprimeTriangulo(n);
    return 0;
}
