#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void toUpper (char *str) {

   for (int i = 0; str[i]; i++) {

      str[i] = toupper (str[i]);
     
   }
  
}

int main(void) {

   int N, M;
  
   scanf("%d", &N);

   char **dicionario = malloc (N * sizeof(char*));
   
   if (dicionario == NULL) {

      printf("Erro: falha na alocação de memória.\n");
     
      return 1;
     
   }

   for (int i = 0; i < N; i++) {

      dicionario[i] = malloc (6 * sizeof(char));

      if (dicionario[i] == NULL) {

         printf("Erro: falha na alocação de memória.\n");

         for (int j = 0; j < i; j++) {

            free(dicionario[j]);
           
         }

         free(dicionario);

         return 1;
        
      }

      scanf("%s", dicionario[i]);
     
   }

   scanf("%d", &M);

   for (int i = 0; i < M; i++) {

      char consulta[6];

      scanf("%s", consulta);

      toUpper (consulta);

      int encontrada = 0;

      for (int j = 0; j < N; j++) {

         if (strcmp(consulta, dicionario[j]) == 0) {

            encontrada = 1;
            break;
           
         }
        
      }

      if (encontrada) {

         printf("%s ok\n", consulta);
        
      } else {

           printf("%s nao existe\n", consulta);
        
        }
     
   }

   for (int i = 0; i < N; i++) {

      free(dicionario[i]);
     
   }

   free(dicionario);

   return 0;
  
}