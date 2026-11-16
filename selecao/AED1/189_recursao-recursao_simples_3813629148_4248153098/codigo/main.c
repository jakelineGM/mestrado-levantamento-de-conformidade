#include <stdio.h>
#define N 12

//Qualquer duvida mande mensagem aos monitores
void andar_para_cima(int mat[N][N], int x, int y, int linhaTamanho, int colunaTamanho){
  if(x < 0 || x >= linhaTamanho || y < 0 || y >= colunaTamanho){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_para_cima(mat, x - 1, y, linhaTamanho, colunaTamanho);
}
void andar_para_baixo(int mat[N][N], int x, int y, int linhaTamanho, int colunaTamanho){
  if(x < 0 || x >= linhaTamanho || y < 0 || y >= colunaTamanho){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_para_baixo(mat, x + 1, y, linhaTamanho, colunaTamanho);
}
void andar_para_direita(int mat[N][N], int x, int y, int linhaTamanho, int colunaTamanho){
  if(x < 0 || x >= linhaTamanho || y < 0 || y >= colunaTamanho){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_para_direita(mat, x, y + 1, linhaTamanho, colunaTamanho);
}
void andar_para_esquerda(int mat[N][N], int x, int y, int linhaTamanho, int colunaTamanho){
  if(x < 0 || x >= linhaTamanho || y < 0 || y >= colunaTamanho){
    return;
  }
  printf("%d ", mat[x][y]);
  andar_para_esquerda(mat, x, y - 1, linhaTamanho, colunaTamanho);
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
andar_para_cima(mat, posiLinha - 1, posiColuna, linhaTamanho, colunaTamanho);

andar_para_baixo(mat, posiLinha + 1, posiColuna, linhaTamanho, colunaTamanho);

andar_para_direita(mat, posiLinha, posiColuna  + 1, linhaTamanho, colunaTamanho);

andar_para_esquerda(mat, posiLinha, posiColuna  - 1, linhaTamanho, colunaTamanho);

  printf("\n");

  
  return  0;
}