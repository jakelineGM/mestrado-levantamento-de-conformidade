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
  int nChaves;
  int qntdChaves;
  int indice;
  int N;
  int valores;

  scanf("%d", &qntdChaves);

  int vetor[qntdChaves];

  for(N = 0; N <qntdChaves; N++){
    scanf("%d", &nChaves);
    vetor[N] = nChaves;
  }

  while(scanf("%d", &valores)){
    indice = buscadorsequencial(vetor, qntdChaves, valores);
    if(indice != -1){
      printf("%d: posicao %d\n", valores, indice);
    } else {
      printf("%d: nao encontrada\n", valores);
    }
  }
}
