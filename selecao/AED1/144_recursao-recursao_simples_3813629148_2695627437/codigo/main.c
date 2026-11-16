#include <stdio.h>
#define N 12

int valida(int i, int j, int linhas, int colunas){
  return (i>=0 && i<linhas && j>=0 && j<colunas);
}

void cima(int mat[N][N], int i, int j, int linhas, int colunas){
  if(valida(i-1,j,linhas,colunas)){
    printf("%d ", mat[i-1][j]);
    cima(mat,i-1,j,linhas,colunas);
  }
}

void baixo(int mat[N][N], int i, int j, int linhas, int colunas){
  if(valida(i+1,j,linhas,colunas)){
    printf("%d ", mat[i+1][j]);
    baixo(mat,i+1,j,linhas,colunas);
  }
}

void direita(int mat[N][N], int i, int j, int linhas, int colunas){
  if(valida(i,j+1,linhas,colunas)){
    printf("%d ", mat[i][j+1]);
    direita(mat,i,j+1,linhas,colunas);
  }
}

void esquerda(int mat[N][N], int i, int j, int linhas, int colunas){
  if(valida(i,j-1,linhas,colunas)){
    printf("%d ", mat[i][j-1]);
    esquerda(mat,i,j-1,linhas,colunas);
  }
}

int main(){
  
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
  cima(mat,posiLinha,posiColuna,linhaTamanho,colunaTamanho);
  baixo(mat,posiLinha,posiColuna,linhaTamanho,colunaTamanho);
  direita(mat,posiLinha,posiColuna,linhaTamanho,colunaTamanho);
  esquerda(mat,posiLinha,posiColuna,linhaTamanho,colunaTamanho);
  printf("\n");
  return  0;
}