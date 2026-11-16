#include <stdio.h>
#define N 12

void imprime_cima(int mat[][N], int linha, int coluna){
  if(linha >= 0 && linha < N){
      printf("%d ", mat[linha][coluna]);
      linha -= 1;
      if(linha >= 0 && linha < N){
          imprime_cima(mat, linha, coluna);
      }
  }
}

void imprime_baixo(int mat[][N], int linha, int coluna, int tam){
  if(linha >= 0 && linha < tam){
      printf("%d ", mat[linha][coluna]);
      linha += 1;
      if(linha >= 0 && linha < tam){
          imprime_baixo(mat, linha, coluna, tam);
      }
  }
}

void imprime_direita(int mat[][N], int linha, int coluna, int tam){
    if(coluna >= 0 && coluna < tam){
        printf("%d ", mat[linha][coluna]);
        coluna += 1;
        if(coluna >= 0 && coluna < tam){
            imprime_direita(mat, linha, coluna, tam);
        }
    }
  
}

void imprime_esquerda(int mat[][N], int linha, int coluna){
    if(coluna >= 0 && coluna < N){
        printf("%d ", mat[linha][coluna]);
        coluna -= 1;
        if(coluna >= 0 && coluna < N){
            imprime_esquerda(mat, linha, coluna);
        }
    }
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
  imprime_cima(mat, (posiLinha-1), posiColuna);
  //baixo
  imprime_baixo(mat, (posiLinha+1), posiColuna, linhaTamanho);
  //direita
  imprime_direita(mat, posiLinha, (posiColuna+1), colunaTamanho);
  //esquerda
  imprime_esquerda(mat, posiLinha, (posiColuna-1));
  printf("\n");
    
  return  0;
}