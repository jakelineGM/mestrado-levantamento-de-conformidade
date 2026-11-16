#include <stdio.h>

int multifatorial(int n, int a) {
  if(n <= 0) {
     return 1;
  }
  return n * multifatorial(n - a, a);
}

int main(void) {
  int n, a;
  int multifat;
  int cont;
  
  while (1){
    scanf("%d %d" ,&n, &a);
    if(n == 0 && a == 0) {
       break;
      
    }  
    multifat = multifatorial(n, a);

    printf("%d", n);
    for(cont = 0; cont < a; cont++) {
        printf("!");
    }
    printf(" = %d\n", multifat); 
}
 return 0;
}

  