#include <stdio.h>
#define N 12

//Qualquer duvida mande mensagem aos monitores
int limites(int linha,int coluna,int linhaTamanho,int colunaTamanho){
  return linha>=0 && linha < linhaTamanho && coluna >=0 && coluna< colunaTamanho;
}

void anda_na_matriz(int matriz[][N],int linha,int coluna,int linhaTamanho,int colunaTamanho){
if(!limites(linha,coluna,linhaTamanho,colunaTamanho)){
  return;
}

  printf("%d ",matriz[linha][coluna]);

  anda_na_matriz(matriz,linha-1,coluna,linhaTamanho,colunaTamanho);  
}

void anda_na_matrizBaixo(int matriz[][N],int linha,int coluna,int linhaTamanho,int colunaTamanho){
if(!limites(linha,coluna,linhaTamanho,colunaTamanho)){
  return;
}

  printf("%d ",matriz[linha][coluna]);

  anda_na_matrizBaixo(matriz,linha+1,coluna,linhaTamanho,colunaTamanho);  
}

void anda_na_matrizD(int matriz[][N],int linha,int coluna,int linhaTamanho,int colunaTamanho){
if(!limites(linha,coluna,linhaTamanho,colunaTamanho)){
  return;
}

  printf("%d ",matriz[linha][coluna]);

  anda_na_matrizD(matriz,linha,coluna+1,linhaTamanho,colunaTamanho);  
}

void anda_na_matrizE(int matriz[][N],int linha,int coluna,int linhaTamanho,int colunaTamanho){
if(!limites(linha,coluna,linhaTamanho,colunaTamanho)){
  return;
}

  printf("%d ",matriz[linha][coluna]);

  anda_na_matrizE(matriz,linha,coluna-1,linhaTamanho,colunaTamanho);  
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
  anda_na_matriz(mat,posiLinha-1,posiColuna,linhaTamanho,colunaTamanho);  
  //baixo
  anda_na_matrizBaixo(mat,posiLinha+1,posiColuna,linhaTamanho,colunaTamanho);  
  //direita
  anda_na_matrizD(mat,posiLinha,posiColuna+1,linhaTamanho,colunaTamanho);  
  //esquerda
   anda_na_matrizE(mat,posiLinha,posiColuna-1,linhaTamanho,colunaTamanho); 
    
  return  0;
}