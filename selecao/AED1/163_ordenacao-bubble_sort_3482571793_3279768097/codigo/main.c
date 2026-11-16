#include <stdio.h>



// Função que implementa o algoritmo Bubble Sort
void bubbleSort(int vetor[], int tamanho) 
{
    for(int i = 0; i < tamanho - 1; i++)
      {
        for(int j = 0; j < tamanho - 1 - i; j++)
          {
            if(vetor[j] > vetor[j + 1])
            {
              //trocar(vetor[j], vetor[j + 1]);
              int temp = vetor[j];
              vetor[j] = vetor[j+1];
              vetor[j+1] = temp;
            }
          }
      }
}

int main() {
    int n;

    // Entrada do tamanho do vetor
    scanf("%d", &n);

    int vetor[n];

    // Entrada dos elementos do vetor
    for (int i = 0; i < n; i++) {
        scanf("%d", &vetor[i]);
    }

    // Ordenando o vetor
    bubbleSort(vetor, n);

    // Imprimindo o vetor ordenado
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }

    return 0;
}