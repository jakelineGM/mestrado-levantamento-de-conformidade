def arvore_busca(raiz, chave):
  # Remova o comando pass abaixo e complete seu código.
  #
  # A função deverá ser recursiva e retornar uma referência
  # para o nó que contém a chave desejada ou None se a chave
  # não estiver presente na árvore
  #print(raiz)
  if raiz == None:  
      return None
  if raiz['valor'] == (chave):
      return raiz['valor']
  if raiz['valor'] < chave:
      return arvore_busca(raiz['dir'], chave)
  else:
      return arvore_busca(raiz['esq'], chave)  


# Lê a árvore e a lista de chaves a serem pesquisadas
arvore = eval(input())
chaves = eval(input())

# Faz a pesquisa e imprime de acordo com a especificação
# do enunciado
for k in chaves:
  if arvore_busca(arvore, k):
    print("Chave", k, "encontrada")
  else:
    print("Chave", k, "nao encontrada")