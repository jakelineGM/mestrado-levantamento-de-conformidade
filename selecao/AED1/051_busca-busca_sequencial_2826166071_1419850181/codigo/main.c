#include <stdio.h>
int buscadorsequencial(int vetor[], int tamanho, int valor){
  int i;

  for(i = 0; i < tamanho; i++){
    if(valor == vetor[i]){
      return i;
    }
  }
  return -1;
}


int main(){

  int nchaves;
  int qntdchaves;
  int indice;
  int n;
  int valores;

  scanf("%d", &qntdchaves);

  int vetor[qntdchaves];

  for (n = 0; n < qntdchaves; n++){
    scanf("%d", &nchaves);
    vetor[n] = nchaves;
  }

  while(scanf("%d", &valores)){
    indice = buscadorsequencial(vetor, qntdchaves, valores);
    if(indice != -1){
      printf("%d: posicao %d\n", valores, indice);
    } else {
      printf("%d: nao encontrada\n", valores);
    }
  } 
}