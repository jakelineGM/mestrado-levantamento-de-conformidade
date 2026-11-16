#include <string.h>

// PARTE A MODIFICAR
// INICIOFUNCAOALUNO
// ESCREVA NESSA ÁREA  A FUNCAO questao05 que deve atender ao enunciado do exercício. 
char questao05(char texto[], char padrao[]) {
  unsigned t = 0, p = 0;
  char c;

  // O índice de retorno no vetor `texto` para casos específicos.
  // Ex.: "abababd#ababd#" falharia sem um ponto de retorno.
  unsigned retorno;
  
  // Ler até atingir (null)
  while ((c = texto[t++]) != 0) {
    if (c == padrao[p]) {  
      if (p == 0)
        retorno = t;
      
      p++;
    } else if (padrao[p] == 0) {
      // O (null) do padrão foi atingido, logo, está contido no texto.
      return 1;
    } else {
      if (p != 0)
        t = retorno;
      
      p = 0;
    }
  }
  
  return padrao[p] == 0;
}

//ENDFUNCAOALUNO


// ABAIXO CODIGO USADO PARA TESTE DA FUNCAO. NÃO MOFIQUE!

#include <stdio.h>



int main() {
  char texto[2000]; // texto onde vamos buscar a string de consulta
  char padrao[100]; // string de consulta
   scanf("%[^#]%*c",texto);
   scanf("%[^#]%*c",padrao);

   if(questao05(texto,padrao)) {
     printf("VERDADEIRO\n");
   }
   else {
     printf("FALSO\n");
   }
   
}