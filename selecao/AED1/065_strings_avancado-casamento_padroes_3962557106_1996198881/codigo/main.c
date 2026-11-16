#include <stdio.h>
#include <string.h>

int eh_substring(char s[], char z[]) {

  int i, j;
  int ts = strlen(s);
  int tz = strlen(z);

  if (ts > tz){
    return 0;
  }

  for (i = 0; i <= tz - ts; i++) {
    for (j = 0; j < ts; j++) {
      if (z[i + j] != s[j]){
        break;
      }
    }
    if (j == ts) {
      return 1;
    }
  }
  return 0;
}

int main(void) {

  char s[205], z[205];

  while (1) {
    scanf("%s", s);

    if (s[0] == 'F') 
      break;

    scanf("%s", z);

    if (eh_substring(s, z))
      printf("SIM\n");
    else
      printf("NAO\n");
  }

  return 0;
}