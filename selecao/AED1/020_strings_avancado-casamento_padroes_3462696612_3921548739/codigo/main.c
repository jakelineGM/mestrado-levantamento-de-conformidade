#include <string.h>

int questao05(char txt[], char key[]){
  
  int tam = strlen(txt);
  int tam2 = strlen(key);
  
  for(int i = 0; i<tam; i++){
    int erruptor = 1;
    int j = i;
    for(int k = 0; k<tam2; k++){
        if(txt[j] != key[k]){
          erruptor = 0;
        }
        j++;
    }
    if(erruptor){return 1;}  
  }

  return 0;
}

#include <stdio.h>

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