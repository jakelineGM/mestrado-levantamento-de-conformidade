def busca_bst(arvore, chave):
  if arvore is None:
    return False

  if.chave == arvore['valor']:
    return True
  elif chave < arvore['valor']:
    return busca_bst(arvore['esq'], chave)
  else:
    return busca_bst(arvore['dir'], chave)

## Entrada

casos = []

while True:
  try:
    linha = input().strip()
  except EOFError:
    break
    
  if not linha:
    continue

  arvore = eval(linha)

  if arvore == {}:
    break

  chaves = eval(input().strip())

  casos.append((arvore, chaves))
  
  
for arvore, chaves in casos:
  encontradas = 0

  for chave in chaves:
      
    if busca_bst(arvore, chave):
      print(f"Chave {chave} encontrada")
      encontradas += 1
    else:
      print(f"Chave {chave} nao encontrada")

  print(f"Encontrei {encontradas} chaves")
  print()
  