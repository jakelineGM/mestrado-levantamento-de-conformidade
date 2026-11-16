#include <stdio.h>
#define N 12

void cima(int mat[N][N], int linha, int coluna, int linhaTam) {
  if(linha < 0) {
    return;
  }
  printf("%d ", mat[linha][coluna]);
  cima(mat, linha - 1, coluna, linhaTam);
}

void baixo(int mat[N][N], int linha, int coluna, int linhaTam) {
  if(linha >= linhaTam) {
    return;
  }
  printf("%d ", mat[linha][coluna]);
  baixo(mat, linha + 1, coluna, linhaTam);
}

void direita(int mat[N][N], int linha, int coluna, int colunaTam){
  if(coluna >= colunaTam) {
    return;
  }
  printf("%d ", mat[linha][coluna]);
  direita(mat, linha, coluna + 1, colunaTam);
}

void esquerda(int mat[N][N], int linha, int coluna){
  if(coluna < 0) {
    return;
  }
  printf("%d ", mat[linha][coluna]);
  esquerda(mat, linha, coluna - 1);
}


int main(){
  //seja livre para mudar o nome na qual você assimilar melhor
  int linhaTam,colunaTam,i,j;
  int posiLinha,posiColuna;
  int mat[N][N];
  
  linhaTam = colunaTam = i = j = posiLinha = posiColuna = 0;//inicializar valores com 0
  
  scanf("%d%d",&posiLinha,&posiColuna);// leitura da posição
  scanf("%d%d",&linhaTam,&colunaTam); // leitura do tamanho da matriz
  
  
  for(i=0;i<linhaTam;i++){
    for(j=0;j<colunaTam;j++){
      scanf("%d",&mat[i][j]);
    }
  }


  //Orde da impressão: cima -> baixo -> direitq -> esquerda
  cima(mat, posiLinha - 1, posiColuna, linhaTam);
  baixo(mat, posiLinha + 1, posiColuna, linhaTam);
  direita(mat, posiLinha, posiColuna + 1, colunaTam);
  esquerda(mat, posiLinha, posiColuna - 1);
      
  return  0;
}