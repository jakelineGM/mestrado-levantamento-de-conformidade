#include <stdio.h>
#include <string.h>

int recebe_str(char *frase, char *subfrase, int tam){
  int s = 0;

  for(int i = 0; i < 200 && subfrase[i] != 0 && s != tam; i++){
  if(frase[s] == subfrase[i]){
    s++;
  }
    else{
      s = 0;
    }
  }
  return s;
}

int main(){
  char frase[201];
  char subfrase[201];

  while(scanf("%s %s", frase, subfrase), frase[0] != 'F'){
     int cont = 0;

  while(frase[cont] != 0){
    cont++;
  }
  
  int achou = recebe_str(frase, subfrase, cont);
  if(achou == cont){
    printf("SIM\n");
  }
  else{
    printf("NAO\n");
    }
  }
}
  