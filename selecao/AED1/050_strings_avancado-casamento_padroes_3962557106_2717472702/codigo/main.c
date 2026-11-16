#include <stdio.h>

int substring(char s[], char z[]) {
  int i, j;

    for (i = 0; z[i] != '\0'; i++) {
      for (j = 0; s[j] != '\0'; j++) {
        if (z[i + j] == '\0' || s[j] != z[i + j]) {
          break;
        }
      } 
      if (s[j] == '\0') {
        return 1;
      }
    }
return 0;
}

int main() {
  char s[201];
  char z[201];

    while(1) {
      scanf("%s", s);
      if (s[0] == 'F') {
        break;
      }
      scanf(" %s", z);

      if(substring(s, z)) {
        printf("SIM\n");
      } else {
        printf("NAO\n");
      }
    }
return 0;
}