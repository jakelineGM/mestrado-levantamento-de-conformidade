#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 
int questao05(char texto[], char padrao[]){
  int tamT = strlen(texto);
  int tamP = strlen(padrao);

  if (tamP > tamT) return 0;
    
  for (int i = 0; i <= tamT - tamP; i++) {
    int j = 0;

    while (j < tamP && texto[i + j] == padrao[j]) {
      j++;
    }

      if (j == tamP) {
        return 1; 
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