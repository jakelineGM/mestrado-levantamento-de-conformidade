#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main() {
    int n, m;

    // --- LEITURA DO DICIONÁRIO ---
    if (scanf("%d", &n) != 1) return 0;

    // Aloca uma matriz de strings dinâmica: N palavras de até 5 caracteres (+1 para o '\0')
    char (*dicionario)[6] = malloc(n * sizeof(*dicionario));
    if (dicionario == NULL) {
        printf("Erro de alocacao de memoria.\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        scanf("%5s", dicionario[i]);
    }

    // --- PROCESSAMENTO DAS CONSULTAS ---
    if (scanf("%d", &m) != 1) {
        free(dicionario);
        return 0;
    }

    char consulta[6];
    for (int i = 0; i < m; i++) {
        scanf("%5s", consulta);

        // Converte a palavra buscada para maiúsculas para padronizar com o dicionário
        for (int j = 0; consulta[j] != '\0'; j++) {
            consulta[j] = tolower((unsigned char)consulta[j]); // Garante correspondência exata
            // Como o enunciado pede a impressão em maiúsculas na saída (%s ok / %s nao existe),
            // vamos converter diretamente para maiúsculas:
            consulta[j] = toupper((unsigned char)consulta[j]);
        }

        // Busca linear simples no dicionário
        int encontrado = 0;
        for (int j = 0; j < n; j++) {
            if (strcmp(consulta, dicionario[j]) == 0) {
                encontrado = 1;
                break;
            }
        }

        // Exibe o resultado conforme a especificação
        if (encontrado) {
            printf("%s ok\n", consulta);
        } else {
            printf("%s nao existe\n", consulta);
        }
    }

    // Libera a memória alocada do dicionário
    free(dicionario);

    return 0;
}
