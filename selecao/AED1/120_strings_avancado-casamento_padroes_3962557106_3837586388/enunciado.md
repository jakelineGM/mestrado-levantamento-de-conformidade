# Substrings

Substring
Dizemos que uma string s é uma substring de outra string z se todos os caracteres de s ocorrem em z de maneira contígua. Por exemplo, a string ODE é uma substring de CODEBENCH, mas não de VOLDEMORT, nem de FRODO.
Escreva uma função que recebe duas strings como entrada e retorna um valor verdadeiro se a primeira for substring da segunda. Faça um programa principal que lê uma série de pares de strings s e z. Para cada par, imprima a mensagem SIM ou a mensagem NAO indicando se s é substring de z. A entrada termina quando s for a palavra FIM.
Cada uma das duas strings terá no máximo 200 caracteres e conterá apenas letras minúsculas e o caracter hífen. Não use soluções prontas, como a função strstr() da linguagem C, a construção  substring in string da linguagem Python ou construções semelhantes dessas ou de outras linguagens.
Dica: não é necessário testar a string inteira com strcmp (em C) ou outras funções para identificar o critério de parada. Basta ver se o primeiro caracter de s é a letra 'F'.
