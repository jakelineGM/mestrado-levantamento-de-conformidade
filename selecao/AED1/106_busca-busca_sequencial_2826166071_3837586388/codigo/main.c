#include <stdio.h>

int buscaSequencial(int chave, int vetor[], int N){
  int numero = -1;
  for (int i = 0; i < N; i++)
    if (chave == vetor[i]){
      return i;
    } return numero;
}
int main(void) {
  int N;
  scanf("%d", &N);
  int vetor[N];
  int chave;
  int buscaSeq;
  for (int i = 0; i < N; i++){
    scanf("%d", &vetor[i]);
  }
  while (scanf("%d", &chave) == 1){
    buscaSeq = buscaSequencial(chave, vetor, N);
    if (buscaSeq == -1){
      printf("%d: nao encontrada\n", chave);
    } else {
      printf("%d: posicao %d\n", chave, buscaSeq);
    }
  }
  return 0;
}
//Só um esboço do que eu entendi.
/*void buscaSequencial(double vetor[], double chave[], int N){
  for (int i = 0; i < N; i++){
    int numero = 00;
    for (int j = i; j < N; j++){
      if (chave[i] == vetor[j]){
        numero = j;
      }
    }
    if (numero != 00) {
      printf("%0.lf: posicao %d\n", chave[i], numero);
    } else if (numero == 00){
      printf("%0.lf: nao encontrada\n", chave[i]);
    }
  }
}*/