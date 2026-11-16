def busca_bst(arvore, chave):
  atual =  arvore
  
  while atual is not None:
    if chave == atual['valor']:
      return True
    elif  chave < atual['valor']:
      atual = atual['esq']
    else:
      atual =  atual['dir']
  
  return False

while True:
  linha_arvore = input().strip()
  
  if linha_arvore == "{}":
    break
    
  arvore = eval(linha_arvore)
  chaves = eval(input().strip())
  encontradas = 0

  for chave in chaves:
    if busca_bst(arvore, chave):
      print(f"Chave {chave} encontrada")
      encontradas += 1
    else:
      print(f"Chave {chave} nao encontrada")
      
  print(f"Encontrei {encontradas} chaves")
  print()
