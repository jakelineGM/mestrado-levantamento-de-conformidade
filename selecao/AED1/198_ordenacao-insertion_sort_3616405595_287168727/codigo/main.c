#include <stdio.h>

void imprimir(int n, int *valores){
  printf("{");
  for(int i = 0; i < n; i++){
    printf("%d", valores[i]);
    if(i < n-1){
      printf(", ");
    }
  }
  printf("}\n");
}
void ordenar(int n, int *elementos){
  int i, j, chave;

  for(i = 1; i < n; i++){
    chave = elementos[i];
    j = i - 1;
    
    while(j >= 0 && elementos[j] > chave){
      if(elementos[j + 1] != elementos[j]){
        elementos[j + 1] = elementos[j];
        imprimir(n, elementos);
      }
      j--;
    }
    if(elementos[j + 1] != chave){
      elementos[j + 1] = chave;
      imprimir(n, elementos);
    }
  }
}
int main(){
  int n;
  scanf("%d", &n);
  int valores[n];
  for(int i = 0; i < n; i++){
    scanf("%d", &valores[i]);
  }
  imprimir(n, valores);
  ordenar(n, valores);
  
  return 0;
}