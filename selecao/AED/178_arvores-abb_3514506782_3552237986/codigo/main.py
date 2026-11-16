def busca_arvore(arvore, valor, encontrados):
  if arvore["valor"] == valor:
    print(f"Chave {valor} encontrada")
    return encontrados + 1
  elif arvore["valor"] > valor:
    if arvore["esq"] is None:
      print(f"Chave {valor} nao encontrada")
      return encontrados
    else:
      encontrados = busca_arvore(arvore["esq"], valor, encontrados)
  elif arvore["valor"] < valor:
    if arvore["dir"] is None:
      print(f"Chave {valor} nao encontrada")
      return encontrados
    else:
      encontrados = busca_arvore(arvore["dir"], valor, encontrados)
  return encontrados

while True:  
  arvore = eval(input())
  if not arvore:
    break
  valores = eval(input())
  encontrados = 0
  for valor in valores:
    encontrados = busca_arvore(arvore, int(valor), encontrados)
  print(f"Encontrei {encontrados} chaves")