#include<stdio.h>
#include<stdlib.h>
#include <ctype.h>
#define TAMANHO 6

void imprimir_vetor(const char *vetor){
    printf("%s ", vetor);
}

void leitura_vetor(char *vetor){
    scanf("%s", vetor);
}

char *alocar_vetor(){
  char *vet = malloc(TAMANHO * sizeof *vet); 
  return vet;
}

void comparacao(char **dicionario, char **consulta, int tam_dic, int tam_con){
  int cont = 0;
  int igual = 0;
  int j = 0;
  for(int i = 0; i < tam_con; i++){
    j = 0;
    igual = 0;
    while(igual < TAMANHO - 1 && j < tam_dic){
      cont = 0;
      igual = 0;
      while(cont < TAMANHO - 1){
        if(toupper(*(consulta[i] + cont)) == toupper(*(dicionario[j] + cont))){
          igual++;
        }
        cont++;
      }
      if(igual == 5){
       printf("%s ok\n", *(dicionario + j));
      }
      j++;
     }
     if(igual < 5){
       for(int c = 0; c < TAMANHO - 1; c++){
         printf("%c", toupper(*(consulta[i] + c)));
       }
       printf(" nao existe\n");
     }
  }
}

int main(void){
  int num_palavras_dic, num_palavras_con;
  char **dicionario;
  char **consulta;
  
  scanf("%d", &num_palavras_dic);
  dicionario = malloc(num_palavras_dic * sizeof *dicionario);
  
  for(int i = 0; i < num_palavras_dic; i++){
    dicionario[i] = alocar_vetor(TAMANHO);
  }
  
  for(int i = 0; i < num_palavras_dic; i++){
    leitura_vetor(dicionario[i]);
  }
  
  scanf("%d", &num_palavras_con);
  consulta = malloc(num_palavras_con * sizeof *consulta);
  
  for(int i = 0; i < num_palavras_con; i++){
    consulta[i] = alocar_vetor(TAMANHO);
  }
  
  for(int i = 0; i < num_palavras_con; i++){
    leitura_vetor(consulta[i]);
  }
  comparacao(dicionario, consulta, num_palavras_dic, num_palavras_con);

   //free
  for(int i = 0; i < num_palavras_dic; i++){
    free(dicionario[i]);
  }
  free(dicionario);
  
  for(int i = 0; i < num_palavras_con; i++){
    free(consulta[i]);
  }
  free(consulta);
}