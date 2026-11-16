def insere(arvore, valor):
    if arvore is None:
      return cria_no(valor)
    elif arvore['valor'] > valor:
      arvore['esq'] = insere(arvore['esq'], valor)
    else:
      arvore['dir'] = insere(arvore['dir'], valor)
    return arvore

def cria_arvore():
    """Cria uma árvore vazia.
    """
    return None


def cria_no(valor):
    """Cria um novo nó que não contém filhos e possui o valor
    especificado no argumento como chave."""
    return {'valor': valor, 'esq': None, 'dir': None}

def pre_ordem(raiz, resultado):
  if raiz:
    resultado.append(str(raiz['valor']))
    pre_ordem(raiz['esq'], resultado)
    pre_ordem(raiz['dir'], resultado)

def in_ordem(raiz, resultado):
  if raiz:
    in_ordem(raiz['esq'], resultado)
    resultado.append(str(raiz['valor']))
    in_ordem(raiz['dir'], resultado)

def pos_ordem(raiz, resultado):
  if raiz:
    pos_ordem(raiz['esq'], resultado)
    pos_ordem(raiz['dir'], resultado)
    resultado.append(str(raiz['valor']))
# Lê o primeiro caso de teste
caso = eval(input())
numero_arvore = 1
# Itera até o último caso
while caso != []:
  arvore = cria_arvore()

  for valor in caso:
    arvore = insere(arvore, valor)

  pre = []
  in_ = []
  pos = []

  pre_ordem(arvore, pre)
  in_ordem(arvore, in_)
  pos_ordem(arvore, pos)

  print(f"Arvore {numero_arvore}")
  print(f"Pre-ordem: {' '.join(pre)}")
  print(f"In-ordem: {' '.join(in_)}")
  print(f"Pos-ordem: {' '.join(pos)}")

  numero_arvore += 1


  caso = eval(input())