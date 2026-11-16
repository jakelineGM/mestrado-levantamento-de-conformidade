#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 

int questao05(char texto[],char palavra[]){
  int i,j, verdade;
  
  for (i=0;i<strlen(texto);i++){
    j=0;
    
    if(texto[i]==palavra[j]){
      verdade=0;
      for (j=0;j<strlen(palavra) && palavra[j]==texto[i];j++){
        i++;
        verdade++;
      }
      if (verdade==strlen(palavra)){
        return 1;
      }
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