#include <stdio.h>
#define N 12

//Qualquer duvida mande mensagem aos monitores
void irCima(int mat[N][N], int l, int c){
  if(l<0)return;
  printf("%d ", mat[l][c]);
  irCima(mat, l - 1, c);
}
void irBaixo(int mat[N][N], int l, int c, int maxL){
  if(l>=maxL)return;
  printf("%d ", mat[l][c]);
  irBaixo(mat, l + 1, c, maxL);
}
void irDireita(int mat[N][N], int l, int c, int maxC){
  if(c>=maxC)return;
  printf("%d ", mat[l][c]);
  irDireita(mat, l ,c + 1, maxC);
}
void irEsquerda(int mat[N][N], int l, int c){
  if(c<0)return;
  printf("%d ", mat[l][c]);
  irEsquerda(mat, l ,c -1);
}
int main(){
  //seja livre para mudar o nome na qual você assimilar melhor
  int linhaTamanho,colunaTamanho,i,j;
  int posiLinha,posiColuna;
  int mat[N][N];
  
  linhaTamanho=colunaTamanho=i=j=posiLinha=posiColuna=0;//inicializar valores com 0
  
  if(scanf("%d%d",&posiLinha,&posiColuna)!=2)return 0;// leitura da posição
  
  if(scanf("%d%d",&linhaTamanho,&colunaTamanho)!=2)return 0; // leitura do tamanho da matriz
  
  
  for(i=0;i<linhaTamanho;i++){
    for(j=0;j<colunaTamanho;j++){
      scanf("%d",&mat[i][j]);
    }
  }
  irCima(mat,posiLinha -1,posiColuna);
  irBaixo(mat,posiLinha + 1,posiColuna, linhaTamanho);
  irDireita(mat,posiLinha, posiColuna + 1, colunaTamanho);
  irEsquerda(mat,posiLinha, posiColuna - 1);

  printf("\n");
  
  return  0;
}