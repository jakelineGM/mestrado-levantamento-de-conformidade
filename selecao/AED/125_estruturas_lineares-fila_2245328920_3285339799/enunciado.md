# O Terminal (Python)

O Terminal
O ano é 1976. Um grupo de alunos precisa fazer um trabalho de programação urgente, mas a universidade não tem um computador para cada um. Em vez disso, os alunos devem fazer uso compartilhado do único terminal que está disponível para eles.
Para que nenhum aluno monopolize o terminal, a turma estabeleceu três regras de uso:
Todos os alunos vão formar uma fila;
Cada aluno pode usar o computador durante Q minutos por vez;
Após Q minutos, se o aluno(a) ainda não tiver completado o trabalho, ele volta pro fim da fila.
Acontece que o terminal tem uma peculiaridade: uma vez que alguém faz login no terminal, a sessão irá durar exatamente Q minutos! Isso significa que, se o aluno(a) completar a tarefa antes do seu tempo expirar, o próximo aluno deverá aguardar a sessão finalizar antes pode fazer uso do terminal.
Agora os alunos estão todos em fila na frente d'O Terminal. O seu trabalho é calcular o tempo necessário para que todos os alunos completem suas tarefas.
A entrada começa com um inteiro Q, indicando a duração de uma sessão n'O Terminal (será um número estritamente positivo).
Na linha seguinte haverá uma sequência de inteiros indicando o tempo que cada aluno precisa para completar o seu trabalho.
Simule a execução d'O Terminal e imprima o tempo necessário para que todos os alunos completem suas tarefas.

## Dicas

Use uma fila para resolver o problema. Cada elemento da fila deve representar quanto tempo um determinado aluno(a) precisa para finalizar o seu trabalho. No início, você deve preencher a fila com os próprios valores da entrada.
Depois, simule o uso do terminal. Retire o primeiro aluno(a) da fila e verifique se ele pode completar o trabalho em Q minutos. Se o tempo da sessão não for suficiente, então ele(a) volta pro fim da fila e aguarda a próxima chance de usar O Terminal.
Observe que não basta somar os tempos dos alunos, pois quando um aluno finaliza o trabalho, pode ser que o próximo tenha que esperar a sessão fechar sozinha antes de poder continuar o seu próprio trabalho. Isso pode ser observado no seguinte caso de exemplo:
20
10 25
Embora o primeiro aluno precise apenas de 10 minutos para realizar o seu trabalho, como o tempo da sessão é Q=20, o segundo aluno precisa aguardar mais 10 minutos antes de começar a usar o terminal. Depois ele precisará de duas sessões, uma de 20 minutos e outra de apenas 5 minutos. Então o tempo total necessário para que os dois alunos completem os trabalhos é 45 minutos ao invés de 35.
