#include <stdio.h>
#define N 12

//Qualquer duvida mande mensagem aos monitores

int valida(int posicao, int limite){
  if(posicao >= 0 && posicao < limite){
    return 1;
  }
  return 0;
}

void cima(int matriz[N][N], int x, int y){
  if(!valida(x, N)){
    return;
  }

  printf("%d ", matriz[x][y]);
  cima(matriz, x - 1, y);
} 

void baixo(int matriz[N][N], int x, int y, int linhas){
  if(!valida(x, linhas)){
    return;
  }

  printf("%d ", matriz[x][y]);
  baixo(matriz, x + 1, y, linhas);
}


void direita(int matriz[N][N], int x, int y, int colunas){
  if(!valida(y, colunas)){
    return;
  }

  printf("%d ", matriz[x][y]);
  direita(matriz, x, y + 1, colunas);
}

void esquerda(int matriz[N][N], int x, int y){
  if(!valida(y, N)){
    return;
  }

  printf("%d ", matriz[x][y]);
  esquerda(matriz, x, y - 1);
}

int main(void){
  int matriz[N][N];
  int x, y;
  int linhas, colunas;
  printf("digite: ");
  scanf("%d %d", &x, &y);
  scanf("%d %d", &linhas, &colunas);

  for(int i = 0; i < linhas; i++){
    for(int j = 0; j < colunas; j++){
      scanf("%d", &matriz[i][j]);
    }
  }

  cima(matriz, x - 1, y);

  baixo(matriz, x + 1, y, linhas);

  direita(matriz, x, y + 1, colunas);

  esquerda(matriz, x, y - 1);

  return 0;
}


