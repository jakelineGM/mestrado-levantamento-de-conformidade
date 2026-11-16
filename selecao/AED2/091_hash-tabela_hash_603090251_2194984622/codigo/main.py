def print_tabela(tabela):
  for index, item in enumerate(tabela):
    if item is not None:
      print(f"{index}: {item}")

def insert_tabela(k, tabela):
  fh(k, tabela)

def fh(k, tabela):
  m = len(tabela)
  assento = k%m
  if tabela[assento] is None:
    tabela[assento] = k
  else:
    assento = fhl(k, tabela, m)
    tabela[assento] = k

def fhl(k, tabela, m):
  assento = k%m

  i=1
  while tabela[(assento+i)%m] is not None:
    i+=1

  return assento+i

m = eval(input())
n = eval(input())
tabela = [None]*m

for i in range(n):
  entrada = eval(input())
  insert_tabela(entrada, tabela)

print_tabela(tabela)