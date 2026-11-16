def cria_arvore(chave):
  return {'valor': chave, 'esq': None, 'dir': None}
def insere(arvore, chave):
  if arvore is None:
    return cria_arvore(chave)
  if arvore['valor'] > chave:
    if arvore['esq'] is None:
      arvore['esq'] = cria_arvore(chave)
      return arvore
    else:
      arvore['esq'] = insere(arvore['esq'], chave)
      return arvore
  else:
    if arvore['dir'] is None:
      arvore['dir'] = cria_arvore(chave)
      return arvore
    else:
      arvore['dir'] = insere(arvore['dir'], chave)
      return arvore
def pre(arvore):
  if arvore is None:
    return
  print("", arvore["valor"], end="")
  pre(arvore['esq'])
  pre(arvore['dir'])
def ordem(arvore):
  if arvore is None:
    return
  ordem(arvore['esq'])
  print("", arvore["valor"], end="")
  ordem(arvore['dir'])
def pos(arvore):
  if arvore is None:
    return
  pos(arvore['esq'])
  pos(arvore['dir'])
  print("", arvore["valor"], end="")

contagem = 0
entrada = eval(input())
while entrada != []:
  contagem+=1
  arvore = None
  for e in entrada:
    arvore = insere(arvore, e)
  print("Arvore", contagem)
  print("Pre-ordem:", end="")
  pre(arvore)
  print()
  print("In-ordem:", end="")
  ordem(arvore)
  print()
  print("Pos-ordem:", end="")
  pos(arvore)
  print()
  entrada = eval(input())