def inserir(raiz, valor):
  if raiz is None:
    return {'valor': valor, 'esq': None, 'dir': None}
  if valor < raiz['valor']:
    raiz['esq'] = inserir(raiz['esq'], valor)
  else:
    raiz['dir'] = inserir(raiz['dir'], valor)
  return raiz

def pre_ordem(raiz):
  if raiz is not None:
    print(raiz['valor'], end=' ')
    pre_ordem(raiz['esq'])
    pre_ordem(raiz['dir'])

def encontrar_sucessor(raiz):
  atual = raiz['dir']
  while atual['esq'] is not None:
    atual = atual['esq']
  return atual['valor']

def remover(raiz, valor):
  if raiz is None:
    return None
  if valor < raiz['valor']:
    raiz['esq'] = remover(raiz['esq'], valor)
  elif valor > raiz['valor']:
    raiz['dir'] = remover(raiz['dir'], valor)
  else:
    if raiz['esq'] is None:
      return raiz['dir']
    elif raiz['dir'] is None:
      return raiz['esq']
      
    sucessor_valor = encontrar_sucessor(raiz)
    raiz['valor'] = sucessor_valor
    raiz['dir'] = remover(raiz['dir'], sucessor_valor)
  return raiz

insercao = eval(input())
remocao = eval(input())

raiz = None
for valor in insercao:
  raiz = inserir(raiz, valor)

print("Arvore inicial:", end=' ')
pre_ordem(raiz)
print()

for valor in remocao:
  raiz = remover(raiz, valor)
  print(f'Depois de remover {valor}:', end=' ')
  if raiz is None:
    print('vazia!')
  else:
    pre_ordem(raiz)
    print()