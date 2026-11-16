#include <stdio.h>

// ASSINATURAS DAS FUNCOES (IMPLEMENTE-AS ABAIXO DA MAIN)

void troca(int*, int*);

int particiona(int*, int, int);

void qSort(int*, int, int);

int k; // variavel global

int main() {
    
    
    int n;
    scanf("%d", &n);

    int arr[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
   scanf("%d", &k);

    qSort(arr, 0, n - 1);

    for (int i = 0; i < k; i++) {
        printf("%d ", arr[i]);
    }

    return 0;
}

void troca(int* a, int* b) {
    const int tmp = *a;
    *a = *b;
    *b = tmp;
}

// FUNCOES QUE VOCE DEVE IMPLEMENTAR



void qSort(int* vet, const int inicio, const int fim) {

 int i = inicio;
 int f = fim;
 int pivo = vet[(inicio+fim)/2];

  while(i<=f){

    while(vet[i] < pivo){i++;}
    while(vet[f] > pivo){f--;}

    if(i <= f){

      int temp = vet[i];
      vet[i] = vet[f];
      vet[f] = temp;
      i++;
      f--;
    }
  }
    

  if(inicio <= f){qSort(vet,inicio,f);}
  if(i <= fim){qSort(vet,i,fim);}
    
  }

  
