#include <stdio.h>
#define N 12

//Qualquer duvida mande mensagem aos monitores

void andar_cima(int mat[N][N], int x, int y, int linhaTamanho){
  if(x < 0 || x >= linhaTamanho || y < 0 || y >= N){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_cima(mat, x - 1, y, linhaTamanho);
}

void andar_baixo(int mat[N][N], int x, int y, int linhaTamanho){
  if(x < 0 || x >= linhaTamanho || y < 0 || y >= N){
  return;
}
printf("%d ", mat[x][y]);
andar_baixo(mat, x + 1, y, linhaTamanho);
}

void andar_direita(int mat[N][N], int x, int y, int colunaTamanho){
  if(y < 0 || y >= colunaTamanho || x < 0 || x >= N){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_direita(mat, x, y + 1, colunaTamanho);
}

void andar_esquerda(int mat[N][N], int x, int y){
  if(y < 0 || x < 0 || y >= N || x >= N){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_esquerda(mat, x, y - 1);
}


int main(){
  //seja livre para mudar o nome na qual você assimilar melhor
  int linhaTamanho,colunaTamanho,i,j;
  int posiLinha,posiColuna;
  int mat[N][N];
  
  linhaTamanho=colunaTamanho=i=j=posiLinha=posiColuna=0;//inicializar valores com 0
  
  scanf("%d%d",&posiLinha,&posiColuna);// leitura da posição
  scanf("%d%d",&linhaTamanho,&colunaTamanho); // leitura do tamanho da matriz
  
  
  for(i=0;i<linhaTamanho;i++){
    for(j=0;j<colunaTamanho;j++){
      scanf("%d",&mat[i][j]);
    }
  }


  //Orde da impressão

  //cima
  andar_cima(mat, posiLinha - 1, posiColuna, linhaTamanho);
  
  //baixo
  andar_baixo(mat, posiLinha + 1, posiColuna, linhaTamanho);
  
  //direita
  andar_direita(mat, posiLinha, posiColuna + 1, colunaTamanho);
  
  //esquerda
  andar_esquerda(mat, posiLinha, posiColuna - 1);
  
    
  return  0;
}