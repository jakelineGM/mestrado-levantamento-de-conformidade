#include <stdio.h>

int substring(char s[], char z[]) {
  int i = 0;
  int j = 0;
  int achou = 0;

  while (z[i] != '\0' && achou == 0) {
    j = 0;
    while (s[j] != '\0' && z[i + j] != '\0' && s[j] == z[i + j]) {
      j++;
    }
    if (s[j] == '\0') {
      achou = 1;
    }
    i++;
  }
  return achou;
}

int main(void) {
  char s[205], z[205];
  while (1) {
    scanf("%s", s);
    if (s[0] == 'F') {
      break;
    }
    scanf("%s", z);
    if (substring(s, z)) {
      printf("SIM\n");
    } else {
      printf("NAO\n");
    }
  }
  return 0;
}