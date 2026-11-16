# Recorrência de Collatz recursiva (3n + 1)

Sequência de Collatz
A conjectura de Collatz é baseada na seguinte relação de recorrência:
f(n)={f(n)=2n​,f(n)=3n+1,​ se n for par se n for ıˊmpar​
Especificamente, a conjectura diz que, para qualquer valor inicial n>0, o valor de feventualmente será 1.
Faça uma função recursiva que dado, um inteiro n>0, retorne o número de termos encontrados até chegar em 1 (incluindo o próprio 1).
Use o seguinte protótipo:
int conta_collatz(int num)
Ela deverá contar quantos termos foram verificados para chegar a num=1.
O programa principal deverá apenas ler um número inteiro da entrada e imprimir a saída da função.

## Dicas

Use o seguinte esquema de redução e conquista:
Se num=1, então a sequência só teve um termo, que foi o número inicial
Caso contrário, então reduza para o próximo número da sequência, calcule quantos termos aparecem na sequência desse novo número e some 1
