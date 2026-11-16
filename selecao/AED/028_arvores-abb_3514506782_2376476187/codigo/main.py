def busca_arvore_binaria(arvore_, chave_):
  if arvore_ is None:
    return False

  if chave_ > arvore_["valor"]:
    return busca_arvore_binaria(arvore_["dir"], chave_)
  elif chave < arvore_["valor"]:
    return busca_arvore_binaria(arvore_["esq"], chave_)
  else:
    return True


arvore = eval(input())

while arvore:
  pesquisar = eval(input())
  encontradas = 0

  for chave in pesquisar:
    encontrada = busca_arvore_binaria(arvore, chave)

    if encontrada:
      encontradas += 1
      print(f"Chave {chave} encontrada")
    else:
      print(f"Chave {chave} nao encontrada")

  print(f"Encontrei {encontradas} chaves")
  print()

  arvore = eval(input())
