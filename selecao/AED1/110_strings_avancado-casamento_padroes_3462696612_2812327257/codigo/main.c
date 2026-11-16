#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
unsigned questao05 (char v[], char v2[]){
  unsigned tamv1 = strlen(v);
  unsigned tamv2 = strlen(v2);
  unsigned i, k;
  if (tamv2 > tamv1){
    return 0;
  }
  for (i = 0; i <= tamv1 - tamv2; i++){
    k = 0;
    while (k < tamv2 && v[i + k] == v2[k]){
      k++;
    }
    if (k == tamv2){
      return 1;
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