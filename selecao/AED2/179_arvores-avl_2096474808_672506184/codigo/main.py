def insere(arvore, valor):
    if arvore is None:
      arvore = cria_no(valor)
      
    elif arvore["valor"] < valor:
      arvore["dir"] = insere(arvore["dir"], valor)
      
    elif arvore["valor"] > valor:
      arvore["esq"] = insere(arvore["esq"], valor)

    arvore["altura"] = 1 + max(altura(arvore["esq"]), altura(arvore["dir"]))

    fator_balanceamento = fb(arvore)
    fator_balanceamento_esq = fb(arvore["esq"])
    fator_balanceamento_dir = fb(arvore["dir"])

    """Caso LL"""

    if fator_balanceamento < -1 and arvore["esq"] is not None and fator_balanceamento_esq <= 0 and valor < arvore["esq"]["valor"]:
      arvore = rotacaoLL(arvore)
      
    """Caso RR"""
    if fator_balanceamento > 1 and arvore["dir"] is not None and fator_balanceamento_dir >= 0 and valor > arvore["dir"]["valor"]:
      arvore = rotacaoRR(arvore)

    """Caso RL"""
    if fator_balanceamento > 1 and arvore["dir"] is not None and fator_balanceamento_dir < 0 and valor < arvore["dir"]["valor"]:
      arvore["dir"] = rotacaoLL(arvore["dir"])
      arvore = rotacaoRR(arvore)

    """Caso LR"""
    if fator_balanceamento < -1 and arvore["esq"] is not None  and fator_balanceamento_esq > 0 and valor > arvore["esq"]["valor"]:
      arvore["esq"] = rotacaoRR(arvore["esq"])
      arvore = rotacaoLL(arvore)
         
    return arvore  


def cria_arvore():
    """Cria uma árvore vazia.
    """
    return None


def cria_no(valor):
    """Cria um novo nó que não contém filhos e possui o valor
    especificado no argumento como chave."""
    return {'valor': valor, 'esq': None, 'dir': None, 'altura': 1}

def rotacaoLL(raiz):
    if raiz is None or raiz["esq"] is None:
      return raiz

    nova_raiz = raiz["esq"]
    raiz["esq"] = nova_raiz["dir"]
    nova_raiz["dir"] = raiz
  
    """atualiza as alturas"""
    raiz["altura"] = 1 + max(altura(raiz["esq"]), altura(raiz["dir"]))
    nova_raiz["altura"] = 1 + max(altura(nova_raiz["esq"]), altura(nova_raiz["dir"]))

    return nova_raiz

def rotacaoRR(raiz):
    if raiz is None or raiz["dir"] is None:
      return raiz

    nova_raiz = raiz["dir"]
    raiz["dir"] = nova_raiz["esq"]
    nova_raiz["esq"] = raiz

    """atualiza as alturas"""
    raiz["altura"] = 1 + max(altura(raiz["esq"]), altura(raiz["dir"]))
    nova_raiz["altura"] = 1 + max(altura(nova_raiz["esq"]), altura(nova_raiz["dir"]))
    return nova_raiz

def altura(raiz):
  if raiz is None:
    return 0
  """max retorna o maior valor entre duas entradas"""
  return raiz["altura"]

def fb(raiz):
  if raiz is None:
    return 0
  return altura(raiz["dir"]) - altura(raiz["esq"])
  
def arvore_busca_preOrdem(raiz):
    if raiz is not None:
      print(raiz["valor"])
      arvore_busca_preOrdem(raiz["esq"])
      arvore_busca_preOrdem(raiz["dir"])

def arvore_busca_posOrdem(raiz):
    if raiz is not None:
      arvore_busca_posOrdem(raiz["esq"])
      arvore_busca_posOrdem(raiz["dir"])
      print(raiz["valor"])

# Lê o primeiro caso de teste
caso = eval(input())
contador = 0

# Itera até o último caso
while caso != []:
    contador = contador + 1
    arvore = cria_arvore()
    for i in range(len(caso)):
      arvore = insere(arvore, caso[i])

    print(f"Arvore {contador}")
    print(f"pre: ")
    arvore_busca_preOrdem(arvore)
    print(f"pos: ")
    arvore_busca_posOrdem(arvore)
    print(" ")
    # Lê o próximo caso de teste
    caso = eval(input())