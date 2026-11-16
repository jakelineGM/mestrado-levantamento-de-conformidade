#include <stdio.h>
#include <string.h>

int eh_substring(char s[], char z[]){
  int len_s=strlen(s);
  int len_z=strlen(z);

  if(len_s>len_z){
    return 0;
  }
  for(int i=0; i<=len_z - len_s; i++){
    int j;
    for(j=0; j<len_s; j++){
      if(z[i+j]!=s[j]){
        break;
      }
    }
    if(j==len_s){
      return 1;
    }
  }
  return 0;
}

int main(void){
  char s[202];
  char z[202];

  while(scanf("%s", s)==1){
    if(strcmp(s, "FIM")==0){
      break;
    }
    scanf("%s", z);
    if(eh_substring(s,z)==1){
      printf("SIM\n");
    }else{
      printf("NAO\n");
    }
  }
  return 0;
}