#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 

int questao05(char texto[], char padrao[]) {
  int tamTexto = strlen(texto);
  int tamPadrao = strlen(padrao);

  int temPadrao = 0;
  
  for(int i = 0; i < tamTexto; i++) {
    if(texto[i] == padrao[0]) {
      temPadrao = 1;
      for(int j = 0; j < tamPadrao && j + i< tamTexto; j++) {
        if(texto[i + j] != padrao[j]) {
          temPadrao = 0;
          break;
        }
      }
      if(temPadrao) return 1;
    }
  }
  return 0;
}

//ENDFUNCAOALUNO


// ABAIXO CODIGO USADO PARA TESTE DA FUNCAO. NÃO MOFIQUE!

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