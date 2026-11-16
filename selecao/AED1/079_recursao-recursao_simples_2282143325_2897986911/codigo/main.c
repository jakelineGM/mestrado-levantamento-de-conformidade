#include <stdio.h>

int conta_collatz(int num)
{
  if (num==1){
    return 1;
  }
  else if (num%2==0){
    return conta_collatz(num/2) +1;
  }else{
    return conta_collatz(3*num+1) +1;
  }
  printf("%d",num);
  return 0; 
}


int main(void)
{
  int n, total;
  scanf("%d",&n);
  total=conta_collatz(n);
  printf("%d\n",total);
  return 0;
}