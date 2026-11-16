#include <stdio.h>
int busca_sequencial(int vetor[], int tamanho, int chave){
  for (int i=0; i<tamanho; i++){
    if ( vetor[i] == chave)
      return i;
  }
  return -1;
}
int main(void){
  int num, i, chave, resultado;
  scanf("%d", &num);
  int vetor[num];
  for (i=0; i< num; i++)
    scanf ("%d", &vetor[i]);
  while(scanf("%d", &chave) ==1){
      resultado= busca_sequencial(vetor, num, chave);
      if(resultado != -1)
        printf("%d: posicao %d\n", chave, resultado);
      else
        printf("%d: nao encontrada\n", chave);
    }
    return 0;

}