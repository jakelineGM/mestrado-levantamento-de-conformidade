#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void maiuscula(char *s){
  for (int i = 0; s[i] != '\0'; i++){
    s[i] = toupper((unsigned char)s[i]);
  }
}

int main(void){
  int N, M;

  scanf("%d", &N);

  char **dic = malloc(N * sizeof(char*));
  for(int i = 0; i < N; i++){
    dic[i] = malloc(6 * sizeof(char));
    scanf("%100s", dic[i]);
    maiuscula(dic[i]);
  }
  scanf("%d", &M);

  char consulta[101];

  for(int i = 0; i < M; i++){
    scanf("%100s", consulta);
    maiuscula(consulta);
    
    int achou = 0;
    
    for(int j = 0; j < N; j++){
      if(strcmp(consulta, dic[j]) == 0){
        achou = 1;
        break;
      }
    }

    if(achou){
      printf("%s ok\n", consulta);
    } else {
      printf("%s nao existe\n", consulta);
    }
  }

    for( int i = 0; i < N; i ++){
      free(dic[i]);
    }
    free(dic);
    return 0;
}