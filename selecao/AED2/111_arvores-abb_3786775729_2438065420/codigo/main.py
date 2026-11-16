def arvore_busca(raiz, chave):
   if raiz == None:
     return None
   elif raiz['valor'] == chave:
     return raiz
   elif  raiz['valor'] > chave:
     return arvore_busca(raiz['esq'], chave)
   else:
     return arvore_busca(raiz['dir'], chave)
   

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