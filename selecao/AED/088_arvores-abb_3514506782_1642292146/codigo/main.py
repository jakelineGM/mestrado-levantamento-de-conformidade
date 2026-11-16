def busca(arvore, chave):
  atual = arvore 
  while atual is not None:
    if chave == atual['valor']:
      return True
    elif chave < atual['valor']:
      atual = atual['esq']
    else:
      atual = atual['dir']
  return False

def processa_caso(arvore, chaves):
  encontrados = 0
  for c in chaves:
    if busca(arvore, c):
      print(f"Chave {c} encontrada")
      encontrados += 1
    else:
      print(f'Chave {c} nao encontrada')
  print(f'Encontrei {encontrados} chaves\n')

def main():
  while True:
    linha = input().strip()
    if linha == "":
      continue

    arvore = eval(linha)

    if arvore == {}:
      break

    chaves = eval(input().strip())

    processa_caso(arvore, chaves)

if __name__ == "__main__":
  main()

  