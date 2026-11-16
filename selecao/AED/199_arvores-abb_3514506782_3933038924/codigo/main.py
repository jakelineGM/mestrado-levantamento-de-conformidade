def busca(arvore, chave):
  if arvore == None:
    return False
  elif arvore['valor'] == chave:
    return True
  elif arvore['valor'] > chave:
    return busca(arvore['esq'], chave)
  else:
    return busca(arvore['dir'], chave)

arvore = eval(input())
while arvore != {}:
  buscas = eval(input())
  count = 0
  for e in buscas:
    if busca(arvore, e):
      print(f'Chave {e} encontrada')
      count+=1
    else:
      print(f'Chave {e} nao encontrada')
  print(f'Encontrei {count} chaves')
  print()
  arvore = eval(input())