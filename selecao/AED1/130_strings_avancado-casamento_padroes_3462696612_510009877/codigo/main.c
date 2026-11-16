#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 

int questao05 (char t[], char p []){
  int tamt = strlen(t);
  int tamp = strlen(p);
  int i=0, j=0, k =0, contador = 0;
  for (i = 0; i <tamt; i++){
    if (t[i] == p[0]){
    contador++;
      k =i+1;
      for (j =1; j<tamp;j++) {
        if (t[k] == p[j]){
          contador++;
          k++;
        }
        
      }
      if (contador == tamp){
        return 1;
      }
    }
    contador = 0;
    k = 0;
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