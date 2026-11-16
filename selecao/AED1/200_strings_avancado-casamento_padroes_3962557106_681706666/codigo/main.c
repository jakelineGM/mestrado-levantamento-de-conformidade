#include <stdio.h>
#include <string.h>

#define MAX 201
#define MAX_LINHAS 201

int eh_substring(char s[],char z[]) {
  int len_s = strlen(s);
  int len_z = strlen(z);

  if(len_s > len_z)
    return 0;

  for(int i = 0; i <= len_z - len_s; i++) {
    int j;
    
     for(j = 0; j < len_s; j++) {
         if(s[j] != z[i + j])
           break;
     }
    if( j == len_s)
      return 1;
  }
  
  return 0;
}

int main(void) {
  char strings[MAX_LINHAS][MAX];
  int total = 0;

  while(1) {
    scanf("%s", strings[total]);
    if(strings[total][0] == 'F')
      break;
    
     total++;

     scanf("%s", strings[total]);
     total++;

    
  }

   for(int i = 0; i < total; i += 2) {
     char *s = strings[i];
     char *z = strings[i + 1];

     if(eh_substring(s, z)) {
       printf("SIM\n");
     } else {
       printf("NAO\n");
     }
   }

  return 0;

}
