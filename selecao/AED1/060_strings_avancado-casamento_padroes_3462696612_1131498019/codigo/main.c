#include <string.h>
#include <stdio.h>
// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 

void transformaEmMinuscula(char texto[]){
  int i;
  for (i=0;i<strlen(texto);i++){
    
    if(texto[i] >= 'A' && texto[i] <= 'Z'){
      texto[i] = texto[i] + 32;
    }
  }
}

char questao05(char texto[], char palavra[]){
  transformaEmMinuscula(texto);
  transformaEmMinuscula(palavra);
  if (strstr(texto, palavra)){
    return 1;
  }
  else{
    return 0;
  }
}

//ENDFUNCAOALUNO


// ABAIXO CODIGO USADO PARA TESTE DA FUNCAO. NÃO MOFIQUE!


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