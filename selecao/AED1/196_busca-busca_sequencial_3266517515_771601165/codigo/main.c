#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main(){

  int n, m;

  scanf("%d", &n);

  char dicionario[n][6];
  
  for (int i = 0; i < n; i++){

    scanf("%s", dicionario[i]);
  }
  
  scanf("%d", &m);

  char consulta[6];

  for (int i = 0; i < m; i++){

    scanf("%s", consulta);

    for(int j = 0; consulta[j] != '\0'; j++){

      consulta[j] = toupper(consulta[j]);
    }

    int encontro = 0;
    for (int j = 0; j < n; j++){

      if(strcmp(consulta, dicionario[j]) == 0){
        encontro = 1;
        break;
      }
    }

    if (encontro){

      printf("%s ok\n", consulta);
    }
    else {

      printf("%s nao existe\n", consulta);
    }
  }
}
  