#include <stdio.h>

// BEGIN
void binSearch (int vet[], int vSize, int value){
  int i, m, f;
  i=0;
  f=vSize-1;
  while (i<=f){
    m=(i+f)/2;
    printf("%d ", vet[m]);
    if (value==vet[m]){
     break;
    }
    else if (value>vet[m]){
      i=m+1;
    }
    else {
      f=m-1;
    } 
  }
}

// END

int main() {
  int vet[] = {3,12,20,25,40,50,55,90,95,99};
  int vSize = sizeof(vet) / sizeof(vet[0]);
  int value;
  scanf("%d",&value);
  binSearch(vet,vSize, value);
}