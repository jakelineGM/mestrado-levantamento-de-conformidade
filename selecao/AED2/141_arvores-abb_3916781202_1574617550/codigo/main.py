def insere(arvore, valor):
  if arvore is None:
    arvore = cria_no(valor)
  elif arvore['valor'] > valor:
    arvore['esq'] = insere(arvore['esq'], valor)
  else:
    arvore['dir'] = insere(arvore['dir'], valor)
  return arvore  

def acha_antecessor(arvore):
  if arvore['dir'] is not None:
    return acha_antecessor(arvore['dir'])
  else:
    return arvore['valor']

def acha_sucessor(arvore):
  if arvore['esq'] is not None:
    return acha_sucessor(arvore['esq'])
  else:
    return arvore['valor']

def arvore_busca(raiz, chave):
  if raiz == None:
    return None
  elif raiz['valor'] == chave:
    antecessor = acha_antecessor(raiz['esq'])
    sucessor = acha_sucessor(raiz['dir'])
    print(f"Chave {raiz['valor']} tem antecessor {antecessor} e sucessor {sucessor}")
  elif raiz['valor'] > chave:
    return arvore_busca(raiz['esq'], chave)
  else:
    return arvore_busca(raiz['dir'], chave)  

def cria_arvore():
  return None

def cria_no(valor):
  return {'valor': valor, 'esq': None, 'dir': None}

arvoreInicial = eval(input())
arvore = cria_arvore()

for i in range(len(arvoreInicial)):
  arvore = insere(arvore, arvoreInicial[i])

chaves = eval(input())
for i in range(len(chaves)):
  arvore_busca(arvore, chaves[i])

