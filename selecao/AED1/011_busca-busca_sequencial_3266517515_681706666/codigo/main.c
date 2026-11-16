#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void to_upper(char *str) {
  for (int i = 0; str[i] != '\0'; i++) {
    str[i] = toupper(str[i]);
  }
}


int main(void) {
  int N, M;
  scanf("%d", &N);

  char **dic = malloc(N * sizeof(char*));

  for(int i = 0; i < N; i++) {
    dic[i] = malloc(6 * sizeof(char));
    scanf("%s", dic[i]);
  }

  scanf("%d", &M);

  char palavra[100];

  for (int i = 0; i < M; i++) {
    scanf("%s", palavra);

    char consulta[6];

    strncpy(consulta, palavra, 5);
    consulta[5] = '\0';

    to_upper(consulta);

    int existe = 0;

    for( int j = 0; j < N; j++) {
      if(strcmp(dic[j],consulta) == 0) {
        existe = 1;
        break;
      }
    }

    if(existe)
      printf("%s ok\n", consulta);
    else 
      printf("%s nao existe\n", consulta);
  }

  for(int i = 0; i < N; i++) {
      free(dic[i]);
  }
  free(dic);

  return 0;

}










  


















  
