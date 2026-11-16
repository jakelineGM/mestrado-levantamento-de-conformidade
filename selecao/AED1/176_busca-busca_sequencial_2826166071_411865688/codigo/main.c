#include <stdio.h>

int buscaSequencial(int vetor[], int N, int chave) {

  for(int i = 0; i < N; i++) {
      if(vetor[i] == chave)
         return i;
  }

  return -1;

}

int main() {

  int N;

  scanf("%d", &N);

  int vetor[N], chave, resultadoBuscaSequencial;

  for(int i = 0; i < N; i++) {
      scanf("%d", &vetor[i]);
  }

  while(scanf("%d", &chave)) {

      resultadoBuscaSequencial = buscaSequencial(vetor, N, chave);

      if(resultadoBuscaSequencial != -1) {
         printf("%d: posicao %d\n", chave, resultadoBuscaSequencial); 
      }
      else {
        printf("%d: nao encontrada\n", chave);
      }
  }

  return 0;

}

