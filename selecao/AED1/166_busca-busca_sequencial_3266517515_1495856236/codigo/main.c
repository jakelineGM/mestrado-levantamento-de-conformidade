#include <stdio.h>
#include <string.h>
#include <ctype.h>

void maiuscula(char string[]){
  for(int i = 0;string[i] != '\0'; i++){
    string[i] = toupper(string[i]);
  }
}

int main(void){

  int tam;
  scanf("%d", &tam);

  char dicionario[tam][6]; // 5 + \0

  for(int i = 0; i < tam; i++){
    scanf("%5s", dicionario[i]);
  }

  int num_consultas;
  scanf("%d", &num_consultas);

  char consulta[6];
  for(int i = 0; i <num_consultas; i++){
    scanf("%5s", consulta);

    maiuscula(consulta);

    int achou = 0;
    
    for(int j = 0; j < tam; j++){
      if(strcmp(consulta,dicionario[j]) == 0){
        
        achou = 1;
        break;
      }  
    }
  
    if(achou)
      printf("%s ok\n", consulta);
    
    else
      printf("%s nao existe\n", consulta);
    
  }
  return 0;
}