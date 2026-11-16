num = int(input())
num2 = int(input())

tabela = [None]*num

for cont in range(num2):
  valor = int(input())
  cont2 = 0
  while True:
    pos = (valor+cont2) % num
    if tabela[pos] is None:
      tabela[pos] = valor
      break
    cont2 += 1

for indice in range(num):
  if tabela[indice] is not None:
    print("%d: %d" % (indice, tabela[indice]))