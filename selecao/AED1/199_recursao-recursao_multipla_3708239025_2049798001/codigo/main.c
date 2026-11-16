#include <stdio.h>

int triangulo_pascal(int linha, int coluna) {
    
  // ESCREVA SEU CÓDIGO AQUI !!!
  if(coluna == 0 || coluna == linha){
    return 1;
  }
  return triangulo_pascal(linha-1, coluna-1)+triangulo_pascal(linha-1, coluna);
}


void imprime_tri_pascal(int linhas) {
  if(linhas == 0) return;
  imprime_tri_pascal(linhas -1);
  // ESCREVA SEU CÓDIGO AQUI !!!
  for(int i = 0; i < linhas -1; i++){
    printf(" ");
  }
    for(int j = 0; j < linhas; j++){
      printf("%d ", triangulo_pascal(linhas -1, j));
}
  printf("\n");
}
int main(void) {
  
    int linhas;
    scanf("%d", &linhas);
    printf("Triangulo de Pascal com %d linhas: \n", linhas);
    imprime_tri_pascal(linhas);
    return 0;
  
}