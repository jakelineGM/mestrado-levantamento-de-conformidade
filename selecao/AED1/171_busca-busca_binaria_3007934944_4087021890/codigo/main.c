#include <stdio.h>

// BEGIN
void binSearch(int vt[], unsigned tam, int chave){
  int inicio =0;
  int fim = tam-1;
  int meio;

  while(inicio<=fim){
    meio= (inicio+fim)/2;
    printf("%d ", vt[meio]);
    if(vt[meio] == chave){
      return;
    }
    else if(chave<vt[meio]){
      fim = meio-1;
    }
    else{
      inicio = meio+1;
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