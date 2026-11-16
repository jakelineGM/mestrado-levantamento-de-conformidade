
def inserir_tabela_hash(tabela,valor,index,tamanho):
  indexValido = (index+valor)%tamanho
  if(tabela[indexValido] == None):
    tabela[indexValido] = valor
  else:
    inserir_tabela_hash(tabela,valor,index+1,tamanho)


tamanho = int(input())
quantidade_valores_hash = int(input())
tabelaIncrivel = [None]*tamanho

for i in range(quantidade_valores_hash):
  hashValue = int(input())
  inserir_tabela_hash(tabelaIncrivel,hashValue,0,tamanho)
  
for i in range(tamanho):
   if tabelaIncrivel[i] != None:
     print(f'{i}: {tabelaIncrivel[i]}')
   
  
  
