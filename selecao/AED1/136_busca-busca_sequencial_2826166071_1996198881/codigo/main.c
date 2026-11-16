#include <stdio.h>

//Função de busca sequencial 
int busca_sequencial(int vetor[], int tamanho, int chave) {

  for (int  i = 0; i < tamanho; i++) {
    if (vetor[i] == chave)
      return i;
  }
  return -1;
}

int main(void) {

  int N;
  scanf("%d", &N);

  int vetor[N];

  for (int i = 0; i < N; i++) {
    scanf("%d", &vetor[i]);
  }

  int chave;

  while (scanf("%d", &chave) == 1) {
    int pos = busca_sequencial(vetor, N, chave);

    if (pos != -1)
      printf("%d: posicao %d\n", chave, pos);
    else
      printf("%d: nao encontrada\n", chave);
  }

  return 0;
}