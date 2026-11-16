# #include <stdio.h>
# #include <stdlib.h>

# typedef struct nodo Nodo;
# struct nodo {
#   int carta;
#   Nodo *prox;
# };


# typedef struct fila Fila;
# struct fila {
#   Nodo *prim;
#   Nodo *fim;
#   int tamanho;
# };


# Fila *cria_fila(void)
# {
#   Fila *nova = malloc(sizeof (Fila));
#   nova->prim = NULL;
#   nova->fim = NULL;
#   nova->tamanho = 0;
#   return nova;
# }


# void insere(Fila *fila, int carta)
# {
#   Nodo *novo = malloc(sizeof(Nodo))
#   novo->carta = carta;
#   novo->prox = NULL;

#   if (fila->fim != NULL):
#     fila->fim->prox=novo;
#   else:
#     fila->prim = novo;
#   fila->fim=novo;
#   fila->tamanho++;

# }



# int retira(Fila *fila)
# {
#    if (fila->prim == NULL){
#      return -1;
#    } 
#    Nodo *removido = fila->prim;
#    int carta = removida->carta;
#    fila->prim = removida->prox;
#    if (fila->prim == NULL){
#      fila->fim = NULL;
#    }
#    free(removido);
#    fila->tamanho--;
#    return carta;
# }


# int tamanho(Fila *fila)
# {
#   return fila->tamanho;
# }


# int main(void)
# {
#   int n;
#   while(1){
#     scanf("%d", &n);
#     if(n==0){
#       break;
#     }
#     Fila *fila = cria_fila();
#     for (int i = 1; i<=n; i++){
#       insere(fila,i);
#     }
#     printf("Descartadas:")
#     int primeira = 1;
#     while (tamanho(fila)>1){
#       int descartada = retira(fila);
#       if(primeira){
#         printf(" %d", descartada);
#         primeira = 0;
#       }
#       else{
#         printf(", %d", descartada);
#       }
#       int para_fundo = retirada(fila);
#       insere(fila,para_fundo);
#     }
#     printf("\nRestou: %d\n\n",retira(fila));
#     free(fila);
#   }
#   return 0;
# }

# def brincar_com_cartas(n):
#   if n ==0:
#     return None, None
#   fila = list(range(1, n +1))
#   descartadas = []
#   while len(fila)> 1:
#     descartadas.append(fila.pop(0))
#     fila.append(fila.pop(0))

#   return descartadas, fila[0]
# entrada = list(map(int, input().strip().split()))

# for n in entrada: 
#   if n == 0:
#     break 
#   descartadas, restou = brincar_com_cartas(n)
#   print()
#   if descartadas:
#     print(f"Descartadas: {', '.join(map(str, descartadas))}")
#   else:
#     print("Descartadas: ")
#   print(f"Restou: {restou}")


def brincar_com_cartas():
  entradas = list(map(int, input().split()))
  for n in entradas:
    if n ==0:
      break 
    monte = list(range(1, n+1))
    descartadas = []


    while len(monte)> 1:
      descartadas.append(monte.pop(0))
      monte.append(monte.pop(0))

    carta_restante = monte[0]

    print("Descartadas:", " ".join(map(str, descartadas)) if descartadas else "")
    print("Restou:", carta_restante)
    print()

brincar_com_cartas()