def criar_no(valor):
  return {'valor': valor, 'esq': None, 'dir': None}

def insere(raiz, valor):
  if raiz is None:
    return criar_no(valor)
  atual = raiz
  while True:
    if valor < atual['valor']:
      if atual['esq'] is None:
        atual['esq'] = criar_no(valor)
        break
      atual = atual['esq']
    else:
      if atual['dir'] is None:
        atual['dir'] = criar_no(valor)
        break
      atual = atual['dir']
  return raiz

def rotacaoRR(t):
  if t is None or t['dir'] is None:
    return t
  y = t['dir']
  t['dir'] = y['esq']
  y['esq'] = t
  return y

def pre_ordem(no, out):
  if no is None:
    return
  out.append(str(no['valor']))
  pre_ordem(no['esq'], out)
  pre_ordem(no['dir'], out)


def pos_ordem(no, out):
  if no is None:
    return
  pos_ordem(no['esq'], out)
  pos_ordem(no['dir'], out)
  out.append(str(no['valor']))

i=1

while True:
  linha = input().strip()

  valores = eval(linha)
  if valores == []:
    break

  t = None
  for x in valores:
    t = insere(t, x)

  t = rotacaoRR(t)
  
  pre = []
  pos = []
  pre_ordem(t, pre)
  pos_ordem(t, pos)

  print(f"Arvore {i}")
  print("pre: " + " ".join(pre))
  print("pos: " + " ".join(pos))
  print()
  i += 1