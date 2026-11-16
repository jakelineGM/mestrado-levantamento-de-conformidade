# Paridade extremamente ineficiente

Paridade Extremamente Ineficiente!
Escreva um programa que usa uma função desnecessariamente recursiva e muito ineficiente para verificar se um número positivo é par ou ímpar.

Considere o seguinte esquema de redução e conquista:
Caso base: n=0 é um número par
Redução: verifique se n-1 é um número par ou ímpar
Conquista: a paridade de n é o inverso da paridade de n-1; isto é, se n-1 é ímpar, então n é par (e a relação é equivalente para par/ímpar)
Faça um programa principal que lê uma sequência de números inteiros. Para cada um deles, imprima uma mensagem indicando se o número é par ou ímpar, seguindo os exemplos. Pare quando um número negativo for digitado.
