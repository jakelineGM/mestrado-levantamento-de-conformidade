#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 

int questao05(char t[],char p[]){
  unsigned i = 0, j = 0;
  unsigned tamt = strlen(t);
  unsigned tamp = strlen(p);

  while(i<=tamt-tamp){
    if((j<tamp)&&(t[i+j]!= p[j])){
      i++;
      j=0;
    }
    else if(j == tamp){
      return 1;
    }
    else{
      j++;
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