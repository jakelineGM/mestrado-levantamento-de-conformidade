tam_m = int(input())
num = int (input())

tabela = [None] * tam_m

for _ in range(num):
  chave = int(input())

  for i in range(tam_m):
    pos = (chave + i) % tam_m

    if tabela[pos] is None:
      tabela[pos] = chave
      break

for cedula in range(tam_m):
  if tabela[cedula] is not None:
    print("%d: %d" % (cedula, tabela[cedula]))

