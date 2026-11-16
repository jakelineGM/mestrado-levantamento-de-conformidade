#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 
int questao05(char texto[], char padrao[]){
  unsigned tamvet = 0;
  int x;
  int y = 0;
  for(x=0;x<2000;x++){
    if(tamvet != strlen(padrao)){
    if(texto[x] == padrao[y]){
      tamvet ++;
      y ++;
    }
    else{
      y = 0;
      tamvet = 0;
    }
  }
}
  if (tamvet == strlen(padrao)){
    return 1;
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