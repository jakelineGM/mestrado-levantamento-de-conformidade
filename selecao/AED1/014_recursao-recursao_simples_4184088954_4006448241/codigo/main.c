#include <stdio.h>
#include <stdbool.h>

int mdc(int a, int b){
  if(b == 0){
    return a;
  }
  else{
    return mdc(b, a % b);
  }
}
int main(){
  int a;
  int b;
  bool parar;
  int result;
  
  //scanf("%d %d", &a, &b);

  parar = true;
  while(parar){
     scanf("%d %d", &a, &b);
    if((a == 0) && (b == 0)){
      parar = false;
    }
    else{
      result = mdc(a, b);
       printf("%d\n", result);

     }
  }
}