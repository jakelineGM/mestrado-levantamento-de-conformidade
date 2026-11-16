#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 


//ENDFUNCAOALUNO
int questao05 (char str[], char chave[]){
  unsigned i, j, tamString, tamChave;

  tamString = strlen(str);
  tamChave = strlen(chave);
  
  for (i=0;i <= (tamString - tamChave); i++){
    for (j=0;j<tamChave;j++){
      if (str[i+j] != chave[j]){
        break;
      }
    }

    if (j == tamChave){
      return 1;
    }
  }

  return 0;
}

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