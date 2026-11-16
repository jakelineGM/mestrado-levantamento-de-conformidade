def busca(arvore, chave):
  if arvore is None:
    return False

  if chave == arvore["valor"]:
    return True
  elif chave < arvore['valor']:
    return busca(arvore['esq'], chave)
  else:
    return busca(arvore['dir'], chave)

def main():
  while True:
    linha = input().strip()

    if linha == "{}":
      break 

    arvore = eval(linha)
    lista = eval(input().strip())

    encontrados = 0

    for chave in lista:
      if busca(arvore, chave):
        print(f"Chave {chave} encontrada")
        encontrados += 1
      else:
        print(f"Chave {chave} nao encontrada")

    print(f"Encontrei {encontrados} chaves")
    

if __name__ == "__main__":
  main()