#include<stdio.h>

int buscaBinaria(int v[], int t, int c) {
  int i = 0, m = 0, f = t - 1;
  int p = 0, u = 0;

  while (i <= f) {
    m = (i + f)/2;
    if (c > v[m]) {
      i = m + 1;
    } else if (c < v[m]) {
      f = m - 1;
    } else {
      p = m;
      f = m - 1;
    }
  }
  
  if (p == 0) {
    return 0;
  } 

  i = 0;
  f = t - 1;

  while (i <= f) {
    m = (i + f)/2;
    if (c > v[m]) {
      i = m + 1;
    } else if (c < v[m]) {
      f = m - 1;
    } else {
      u = m;
      i = m + 1;
    }
  }
  
  if (p == u) {
    return 1;
  } else {
    return 0;
  }
}

void ler(int *v, int size) {
  for (int i = 0; i < size; i++)
    scanf("%d%*c", &v[i]);
}

int main() {
  int chave;
  int size;
  scanf("%d%*c",&chave);
  scanf("%u%*c",&size); // tamanho do vetor
  int vet[size];
  ler(vet,size);
  if (buscaBinaria(vet, size, chave)) {
    printf("SIM");
  } else {
    printf("NAO");
  }
}