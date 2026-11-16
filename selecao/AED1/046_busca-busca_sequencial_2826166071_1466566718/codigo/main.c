#include <stdio.h>

int buscaSeq(int v[], int n, int chave){
  for(int i = 0; i < n; i++){
    if (v[i] == chave)
      return i;
  }
  return -1;
}

int main(void) {
  int n, chave;
  printf(" ");
  scanf("%d", &n);

  int v[n];
  for (int i = 0; i < n; i++)
    scanf("%d", &v[i]);

  printf(" ");
  
  while(1) {
    printf(" ");
    if(scanf("%d", &chave) != 1)
      break;

    int pos= buscaSeq(v,n, chave);
    if( pos == -1)
      printf("%d: nao encontrada\n", chave);
    else
      printf("%d: posicao %d\n", chave, pos);
  }
  return 0;
}