def insereTabelaHash(lista, numero, quantidadeDeValores):
  index = numero % len(lista)
  if lista[index] == -1:
    lista[index] = valor 
  else:
    i = (index + 1) % len(lista)
    while lista[i] != -1:
      i = (i + 1) % len(lista)
    lista[i] = valor

    
tamanhoDaTabela = int(input())
quantidadeDeValores = int(input())

lista = []
for i in range(tamanhoDaTabela):
  lista.append(-1)

for i in range(quantidadeDeValores):
  valor = int(input())
  insereTabelaHash(lista, valor, quantidadeDeValores)

for i in range(len(lista)):
  if lista[i] != -1:
    print(f'%d: %d' % (i, lista[i]))