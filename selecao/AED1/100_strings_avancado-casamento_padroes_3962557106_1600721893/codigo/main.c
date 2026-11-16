#include <stdio.h>
#include <string.h>

int ehSubstring(char s[], char z[]) {
  int ns = strlen(s);
  int nz = strlen(z);

  for (int i = 0; i <= nz - ns; i++) {
    int j = 0;
    while (j < ns && s[j] == z[i + j]) {
      j++;
    }

    if (j == ns)
      return 1;
  }

  return 0;
}

int main() {
  char s[205], z[205];

  scanf("%s", s);

  while(s[0] != 'F') {
    scanf("%s", z);

    if(ehSubstring(s, z)) {
      printf("SIM\n");
    } else {
      printf("NAO\n");
    }

    scanf("%s", s);
  }
  
  return 0;
}