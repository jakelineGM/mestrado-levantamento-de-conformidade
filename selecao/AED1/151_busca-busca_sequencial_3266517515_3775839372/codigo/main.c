#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void maiusculo (char *str)
{
  for (int i = 0; str[i]; i++) {
      str[i] = toupper((unsigned char)str[i]);
  }
}

int main (void)
{
  int N;
  int M;
  char **dicionario;
  int soma;
  
  scanf("%d", &N);
  dicionario = malloc(N * sizeof(char *));
  
  if (dicionario == NULL) {
      printf("Erro");
      return 1;
  }
  for (int i = 0; i < N; i++) {
      dicionario[i] = malloc(6 * sizeof(char));
      scanf("%s", dicionario[i]);
  }
  
  scanf("%d", &M);
  soma = N + M; // delimitei o vetor;
  char consulta[soma];
  
  for (int i = 0; i < M; i++) {
      scanf("%s", consulta);
      maiusculo(consulta);
      int encontrado = 0;
      for (int j = 0; j < N; j++) {
          if (strcmp(consulta, dicionario[j]) == 0) {
               encontrado = 1; 
          }
      }
      if (encontrado == 1) {
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