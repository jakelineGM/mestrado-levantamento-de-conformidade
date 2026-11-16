#include <stdio.h> 

int busca(int vetor[], int tamanho, int chave){
    for(int i = 0; i < tamanho; i++){
      if(vetor[i] == chave){
        return (i);
      }
    }
  return -1;
}

void leitura(int vetor[], int tamanho){
  for(int n = 0; n < tamanho; n++){
    scanf("%d", &vetor[n]);
  }
}
int main(){
  
  int valor;
  int chave;

  scanf("%d", &valor);
  int vetor[valor];
  leitura(vetor, valor);
  
    while(scanf("%d", &chave) == 1 ){
    int posicao;
    posicao = busca(vetor, valor, chave);
      
    if(posicao == -1){
      printf("%d: nao encontrada\n", chave);
    }
    else{
      printf("%d: posicao %d\n", chave, posicao);
    }
  }
}