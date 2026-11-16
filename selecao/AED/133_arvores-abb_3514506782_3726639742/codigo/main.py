def busca_na_arvore(arvore, chave):
    """Busca uma chave na árvore binária de busca."""
    if arvore is None:
        return False
    if arvore['valor'] == chave:
        return True
    elif chave < arvore['valor']:
        return busca_na_arvore(arvore['esq'], chave)
    else:
        return busca_na_arvore(arvore['dir'], chave)

def processa_entrada():
    while True:
        try:
            arvore = eval(input().strip())
            if arvore == {}:
                break
            chaves = eval(input().strip())
            
            chaves_encontradas = 0
            for chave in chaves:
                if busca_na_arvore(arvore, chave):
                    print(f"Chave {chave} encontrada")
                    chaves_encontradas += 1
                else:
                    print(f"Chave {chave} nao encontrada")
            
            print(f"Encontrei {chaves_encontradas} chaves")
            print("")  # Linha em branco para separar os casos
            
        except EOFError:
            break

# Função principal
if __name__ == "__main__":
    processa_entrada()