#include <stdio.h>
#include <string.h>

int verifica_substring(char trecho_pequeno[], char texto_grande[]);

int main(void)
{
  char texto[201];
  char trecho[201];

  while(1){
    scanf("%s",trecho);

    if(trecho[0]=='F'){
      break;
    }

    scanf("%s",texto);

    if(verifica_substring(trecho,texto)){
      printf("SIM\n");
    }else{
      printf("NAO\n");
    }
  }
}


int verifica_substring(char trecho_pequeno[],char texto_grande[])
{
  int tamanho_trecho = strlen(trecho_pequeno);
  int tamanho_texto = strlen(texto_grande);

  for (int i=0;i<tamanho_texto;i++){
    
    if (texto_grande[i]==trecho_pequeno[0]){
      int eh_substring=1;

      for (int j=0;j<tamanho_trecho;j++){
        if (texto_grande[i+j]!= trecho_pequeno[j]){
          eh_substring=0;
          break;
        }
      }
      if (eh_substring == 1){
        return 1;
      }
    }
  }
  return 0;
}