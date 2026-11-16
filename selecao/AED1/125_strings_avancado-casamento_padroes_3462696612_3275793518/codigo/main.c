#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 
int questao05 ( char string[], char pattern[]){
unsigned i;
unsigned j;
  for(i = 0; string[i] != 0; i++){
if(string[i] == pattern[0]){
  for(j = 1; pattern[j] != 0 && pattern[j] == string[i + j]; j++){}
    }
    i = i + j -1;
    if(pattern[j] == 0){
  return(1);
  }
}
return(0);
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