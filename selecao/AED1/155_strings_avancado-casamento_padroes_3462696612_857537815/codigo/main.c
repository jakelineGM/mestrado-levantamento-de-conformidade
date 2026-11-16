#include <string.h>
#include <stdio.h>

unsigned questao05 (char texto[], char padrao[]){
  int txt = strlen(texto);
  int pdr = strlen(padrao);
  int i,j,k;
  for (i = 0; i <= txt-pdr; i++){
    k = 1;
    for (j = 0;j < pdr; j++){
      if (texto[i+j] != padrao[j]){
        k = 0;
     }
    }
    if (k == 1){
      return 1;
    }
  } return 0;
}


int main() {
  char texto[2000]; // texto onde vamos buscar a string de consulta
  char padrao[100]; // string de consulta
   scanf("%[^#]%*c",texto);
   scanf("%[^#]%*c",padrao);

   if(questao05(texto,padrao)) {
     printf("VERDADEIRO\n");
   }
   else {
     printf("FALSO\n");
   }
   
}