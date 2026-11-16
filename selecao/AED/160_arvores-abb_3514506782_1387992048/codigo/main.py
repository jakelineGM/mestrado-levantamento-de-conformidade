def busca_arvore(arvore, chave):
  if arvore is None:
    return False
  if arvore['valor'] == chave:
    return True
  elif chave < arvore['valor']:
    return busca_arvore(arvore['esq'], chave)
  else:
    return busca_arvore(arvore['dir'], chave)

while True:
  arvore = eval(input().strip())

  if arvore == {}:
    break

  chaves = eval(input().strip())

  chaves_encontradas = 0

  for chave in chaves:
    if busca_arvore(arvore, chave):
      print(f"Chave {chave} encontrada")
      chaves_encontradas += 1
    else:
      print(f"Chave {chave} nao encontrada")

  print(f"Encontrei {chaves_encontradas} chaves")
  print()