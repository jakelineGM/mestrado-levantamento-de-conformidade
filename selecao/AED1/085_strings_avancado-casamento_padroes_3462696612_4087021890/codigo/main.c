#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 

int questao05(char texto[], char padrao[] ){
  int i,j;
  int tamtext = strlen(texto);
  int tampadrao = strlen(padrao);
  int encontrou;

  for(i =0; i<=tamtext - tampadrao ; i++){
    encontrou =1;
    for (j=0;j<tampadrao;j++){
      if(texto[i+j] != padrao[j]){
        encontrou = 0;
        break;
      }
      
    }
      if(encontrou ==1){
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