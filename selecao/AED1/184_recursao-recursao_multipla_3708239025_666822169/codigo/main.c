#include <stdio.h>

int triangulo_pascal(int linha, int coluna) {
  int num=0;
  if(coluna==0 || linha==coluna){
    num=1;
  }else{
   num=triangulo_pascal(linha-1,coluna)+triangulo_pascal(linha-1,coluna-1);
  }
  return num;
}


void imprime_tri_pascal(int linhas) {

  for(int i=0;i<linhas;i++){
    for(int k=0;k<linhas-i;k++){
      printf(" ");
    }
     for(int j=0;j<i+1;j++){
      printf("%d ",triangulo_pascal(i,j));
     }
    printf("\n");
  }
  
}

int main(void) {
  
    int linhas;
    scanf("%d", &linhas);
    printf("Triangulo de Pascal com %d linhas:\n", linhas);
    imprime_tri_pascal(linhas);
    return 0;
  
}