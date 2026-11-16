def cria_arvore():
  return None

def insere_arvore(arvore, chave):
  if arvore is None:
    arvore = cria_no(chave)
  elif arvore['valor'] > chave:
    arvore['esq'] = insere_arvore(arvore['esq'], chave)
  else:
    arvore['dir'] = insere_arvore(arvore['dir'],chave)
  atualiza_no(arvore)
  arvore = rotacao(arvore)
  return arvore
  
def cria_no(valor):
  return {'valor': valor,'h':0,'fb':0, 'esq': None, 'dir': None}

def atualiza_no(no):
  if no is not None:
    hDir = retorna_altura(no['dir'])
    hEsq = retorna_altura(no['esq'])
    if hDir > hEsq:
      no['h'] = hDir + 1
    else: no['h'] = hEsq + 1
    no['fb'] = hDir - hEsq
    
def retorna_altura(arvore):
  if arvore is None:
    return 0
  else:
    return arvore['h']

def retorna_fb(arvore):
  if arvore is None:
    return 0
  else:
    return retorna_altura(arvore['dir']) - retorna_altura(arvore['esq'])

def pre_ordem(raiz):
  if raiz is None:
    return
  else:
    print(raiz['valor'], end=' ')
    pre_ordem(raiz['esq'])
    pre_ordem(raiz['dir'])


def pos_ordem(raiz):
  if raiz is None:
    return
  else:
    pos_ordem(raiz['esq'])
    pos_ordem(raiz['dir'])
    print(raiz['valor'], end=' ')

def rotacao(arvore):
  if arvore is None:
    return None
  fbArvore_dir = retorna_fb(arvore['dir'])
  fbArvore_esq = retorna_fb(arvore['esq'])
  if arvore['fb'] > 1:
    if fbArvore_dir >= 0:
      arvore = rotacaoRR(arvore)
    else:
      arvore['dir'] = rotacaoLL(arvore['dir'])
      arvore = rotacaoRR(arvore)
  elif arvore['fb'] < -1:
    if fbArvore_esq <= 0:
      arvore = rotacaoLL(arvore)
    else:
      arvore['esq'] = rotacaoRR(arvore['esq'])
      arvore = rotacaoLL(arvore)
  return arvore

def rotacaoRR(subarvore):
  nova_raiz = cria_arvore()
  nova_raiz = subarvore['dir']
  subarvore['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = subarvore
  atualiza_no(subarvore)
  atualiza_no(nova_raiz)
  return nova_raiz

def rotacaoLL(subarvore):
  nova_raiz = cria_arvore()
  nova_raiz = subarvore['esq']
  subarvore['esq'] = nova_raiz['dir']
  nova_raiz['dir'] = subarvore
  atualiza_no(subarvore)
  atualiza_no(nova_raiz)
  return nova_raiz

lista = eval(input())
cont = 1
while lista != []:
  print(f'Arvore {cont}')
  arvore = cria_arvore()
  for i in range(len(lista)):
    arvore = insere_arvore(arvore,lista[i])
  print("pre: ", end='')
  pre_ordem(arvore)
  print()
  print("pos: ",end='')
  pos_ordem(arvore)
  print()
  lista = eval(input())
  cont += 1
  
  