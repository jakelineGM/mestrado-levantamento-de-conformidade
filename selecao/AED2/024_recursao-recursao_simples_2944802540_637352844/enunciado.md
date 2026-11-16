# Propriedade de Codibentinho

Propriedade de Codibentinho
Codibentinho quer ficar famoso. Para isso, ele inventou o conceito de propriedade de Codibentinho. Um número que obedece à propriedade de Codibentinho é dito ser um número de Codibentinho. Para que um número inteiro n seja considerado de Codibentinho, ele deve respeitar as seguintes regras:
Todo número menor que 5 é um número de Codibentinho;
Todo número que é múltiplo de 17 é um número de Codibentinho;
Se n for divisível por 5, mas não por 17, então será um número de Codibentinho se e somente se n/5 for um número de Codibentinho;
Se n for um número ímpar não divisível por 5, nem por 17, então será um número de Codibentinho se e somente se n - 3 for um número de Codibentinho;
Caso não satisfaça nenhuma das condições anteriores, então não é um número de Codibentinho.
Escreva uma função recursiva para identificar se um número inteiro é um número de Codibentinho ou não.
Escreva um programa que lê dois números inteiros n,m e imprime todos os números de Codibentinho no intervalo fechado [n, m]. Considere que n e m serão maiores que zero e n ≤ m.

## Dicas

Por exemplo, n=4 é um número de Codibentinho porque é menor que 5. O número n=20 também é de Codibentinho, pois 20/5=4 é um número de Codibentinho.
O número n=34 é um múltiplo de 17, portanto é um número de Codibentinho. Consequentemente, n=37 é um número de Codibentinho, pois embora não seja divisível por 17, nem por 5, é ímpar e 37-3=34 é um número de Codibentinho.
Em contrapartida, n=9 não é um número de Codibentinho, pois não satisfaz nenhuma das regras. Além disso, n=45 também não é um número de Codibentinho, pois, embora seja um múltiplo de 5, o número 45/5=9 não é um número de Codibentinho.
Similarmente, n=12 não é número de Codibentinho, pois não é múltiplo de 17, não é múltiplo de 5 e, embora seja ímpar, 12-3=9 não é um número de Codibentinho.
