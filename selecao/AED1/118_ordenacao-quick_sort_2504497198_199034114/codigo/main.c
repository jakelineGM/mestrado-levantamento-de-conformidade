#include <stdio.h>

typedef struct {
    char nome[30];
    char endereco[20];
    float altura; 
} tipoPessoa;

void inserirPessoas(tipoPessoa v[], int tam) {
    for (int i = 0; i < tam; i++) {
        scanf("%[^\n]%*c", v[i].nome); 
        scanf("%[^\n]%*c", v[i].endereco);  
        scanf("%f%*c", &v[i].altura);  
    }
}

void mostrarPessoas(tipoPessoa v[], int tam) {
    for (int i = 0; i < tam; i++) {
        printf("%s\n", v[i].nome);
        printf("%s\n", v[i].endereco);
        printf("%.2f\n", v[i].altura); 
    }
}


// MODIFIQUE A FUNÇÃO AQUI 

void quickSortR(tipoPessoa v[], int inicio, int fim){
  int i,j;
  tipoPessoa pivot, temp;
  i = inicio;
  j = fim;
  pivot = v[(inicio+fim)/2];
  while(i<=j){
    while(v[i].altura > pivot.altura){i++;}
    while(v[j].altura < pivot.altura){j--;}
    if(i<=j){
      temp = v[i];
      v[i] = v[j];
      v[j] = temp;
      i++;
      j--;
    }
  }

  if(inicio < j) quickSortR(v, inicio, j);
  if(i<fim) quickSortR(v,i, fim);
}

void quickSort(tipoPessoa v[], int tam){
  if(tam>0){
    quickSortR(v,0,tam-1);
  }
}

// END FUNCAO

int main() {
    int tam;
    scanf("%d%*c", &tam);  
    tipoPessoa vetor[tam];

    inserirPessoas(vetor, tam);

    // FACA A CHAMADA DA FUNCAO AQUI
    quickSort(vetor,tam);
    // END CHAMADA DA FUNCAO

    mostrarPessoas(vetor, tam);

    return 0;
}