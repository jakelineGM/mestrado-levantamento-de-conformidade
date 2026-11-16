#include <stdio.h>

int substring(const char *s, const char *z){

  int tamS = 0;
  int tamZ = 0;

  for(int i = 0; i<200 && s[i] != 0; i++){
    tamS++;
  }
  for(int i = 0; i<200 && z[i] != 0; i++){
    tamZ++;
  }

  int flag = tamS;
  int j = 0;

  for(int i = 0; i<tamZ && flag != 0; i++){
    if(s[j] == z[i]){
      flag--;
      j++;
    }
    else{
      j = 0;
      flag = tamS;
    }
  }
  return flag;
}

int main(void){
  char s[201];
  char z[201];

  while(scanf("%s %s", s, z), s[0] != 'F'){
    
    if(substring(s, z) == 0){
      printf("SIM\n");
    }
    else{
      printf("NAO\n");   
    }
  }
}