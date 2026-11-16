def busca_chave(arvore, chave):
  if arvore is None:
    return False
  if arvore['valor'] == chave:
    return True
  elif chave < arvore['valor']:
    return busca_chave(arvore['esq'], chave)
  else:
    return busca_chave(arvore['dir'], chave)

while True:
  entrada = input().strip()
  if entrada == '{}':
    break

  arvore = eval(entrada)
  chaves = eval(input().strip())
  chaves_encontradas = 0

  for chave in chaves:
    if busca_chave(arvore, chave):
      print(f"Chave {chave} encontrada")
      chaves_encontradas+=1
    else:
      print(f"Chave {chave} nao encontrada")
  print(f"Encontrei {chaves_encontradas} chaves")