def calcular_hash (chave, tam_tabela):
  return chave % tam_tabela

tam_tabela= int(input())
qttd_chave = int(input())
tabela= [-1]*tam_tabela

for i in range(qttd_chave):
  chave=int(input())
  #ve o indice ideal, se nao tiver ocupado vai p la
  pos=calcular_hash(chave, tam_tabela)
  #colisao, ja ta ocupado
  while tabela[pos]!=-1:
    pos=(pos+1) % tam_tabela

  tabela[pos]=chave
    

for i in range(tam_tabela):
  if tabela[i] !=-1:
     print("%d: %d" % (i, tabela[i]))