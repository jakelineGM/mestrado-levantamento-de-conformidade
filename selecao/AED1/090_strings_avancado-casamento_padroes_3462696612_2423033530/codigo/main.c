#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
    char questao05(char texto[], char padrao[]) {
      int cont, contp;
      int tam = strlen(texto), tamp = strlen(padrao);
      for(cont = 0;cont < tam; cont++ ) {

        if (texto[cont] == padrao[0]) {
          for(contp = 1; contp < tamp; contp++) {
            if (texto[contp + cont] != padrao[contp]) {
              break;
            }
          }
          if(contp == tamp) {
            return 1;
          }
        }
      }
          return 0;
      
    }
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 


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