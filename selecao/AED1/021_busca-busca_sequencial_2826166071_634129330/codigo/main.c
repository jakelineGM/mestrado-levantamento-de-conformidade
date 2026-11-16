#include <stdio.h>
#include <stdlib.h>

int busca(int vetor[], int n, int chave) {
    for (int i = 0; i < n; i++) {
        if (vetor[i] == chave) {
            return i; }  }
    return -1;  
}
int main() {
    int n;
    if (scanf("%d", &n) != 1) {
        return 0;  }
    int *vetor = (int *)malloc(n * sizeof(int));
    if (vetor == NULL) {
        return 1; }
    for (int i = 0; i < n; i++) {
        scanf("%d", &vetor[i]); }
    int chave;
    int posicao;
    while (scanf("%d", &chave) == 1) {
        posicao = busca(vetor, n, chave);
        if (posicao != -1) {
            printf("%d: posicao %d\n", chave, posicao);
        } else {    
            printf("%d: nao encontrada\n", chave); } }
    free(vetor);
    return 0;  
}
