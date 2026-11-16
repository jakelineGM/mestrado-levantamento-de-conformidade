#include <stdio.h>

void binSearch(int v[], int vS, int val) {
  int i = 0, f = vS - 1;

  while (i <= f) {
    int m = (i + f)/2;
    printf("%d " , v[m]);
    if (val > v[m]) {
      i = m + 1;
    } else if (val < v[m]) {
      f = m - 1;
    } else {
      break;
    }
  }
}

int main() {
  int vet[] = {3,12,20,25,40,50,55,90,95,99};
  int vSize = sizeof(vet) / sizeof(vet[0]);
  int value;
  scanf("%d",&value);
  binSearch(vet,vSize, value);
}