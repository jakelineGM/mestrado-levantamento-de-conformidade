#include <stdio.h>
#include <string.h>

int combina(char abre, char fecha) {
  if (abre == '(' && fecha == ')') return 1;
  if (abre == '[' && fecha == ']') return 1;
  if (abre == '{' && fecha == '}') return 1;
  return 0;
}

void checa_balanceamento(char *s) {
  char pilha[101];
  int topo = -1;
  int erro = 0;

  for (int i = 0; s[i] != '\0' && erro == 0; i++) {
    char atual = s[i];

    if (atual == '(' || atual == '[' || atual == '{') {
      topo++;
      pilha[topo] = atual;
    } else if (atual == ')' || atual == ']' || atual == '}') {
      if (topo == -1 || !combina(pilha[topo], atual))
        erro = 1;
      else 
        topo--;
    }
  }

  if (erro == 0 && topo == -1) 
    printf("SIM\n");
  else
    printf("NAO\n");
}

int main() {
  char sequencia[105];

  while(scanf("%s", sequencia) == 1 &&
        strcmp(sequencia, ".") != 0) {
    checa_balanceamento(sequencia);
  }

  return 0;
}