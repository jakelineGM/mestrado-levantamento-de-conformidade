#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 
unsigned questao05 (char vet[], char base []) {
  for (unsigned x = 0; x < strlen(vet); x++) {
    if (vet[x] == base[0]) {
      unsigned flag = 1;
      unsigned y = x;
      for (unsigned z = 0 ; z < strlen(base); z++) {
        if (vet[y] != base[z]) {
          flag = 0;
        }
        y++;
      }
      if (flag == 1) {
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