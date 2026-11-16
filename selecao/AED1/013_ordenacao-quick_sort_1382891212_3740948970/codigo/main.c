#include <stdio.h>

int k; // variavel global pra nao ter que passar como parametro pro qSort

// BEGIN
void quickSelect(int vet[], int inicio, int fim) {
  int i, j, pivot, tmp;
  if(inicio < fim){
    pivot = vet[(inicio+fim)/2];
    i = inicio; j = fim;
    while(i<=j){
      while(vet[i]<pivot) i++;
      while(vet[j]>pivot) j--;
      if(i<=j){
        tmp=vet[i];
        vet[i]=vet[j];
        vet[j]=tmp;
        i++; j--;
      }
    }
  if(k-1 <= j){
    quickSelect(vet,inicio,j);
  }
  else if(k-1>=i) {
    quickSelect(vet,inicio,j);
    quickSelect(vet,i,fim);
  }
  }
}
void qSortKSmallest(int arr[], int len) {
  if(k>0 && k<=len){
    quickSelect(arr, 0, len-1);
  }
}
// END

int main() {
    int len;
    scanf("%d", &len);

    int arr[len];
    for (int i = 0; i < len; i++)
        scanf("%d%*c", &arr[i]);

    scanf("%d%*c", &k);

    qSortKSmallest(arr, len);

    for (int i = 0; i < k; i++)
        printf("%d ", arr[i]);
}