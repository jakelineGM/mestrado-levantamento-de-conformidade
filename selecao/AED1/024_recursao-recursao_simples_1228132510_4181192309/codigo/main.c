#include <stdio.h>
#include <math.h>

double recursaoRaiz(double x,double y,double z){
  if(fabs (y*y -x)<=z){
    return y;
  }
  else{
     return recursaoRaiz (x,(y*y +x)/(2*y),z);
  }
}

int main(void){

  int num;

  scanf("%d ",&num);
  
  while(num--){
    double x,y,z;
    scanf("%lf %lf %lf",&x,&y,&z);
    printf("%.5lf\n",recursaoRaiz(x,y,z));
  }
  return 0;
}


