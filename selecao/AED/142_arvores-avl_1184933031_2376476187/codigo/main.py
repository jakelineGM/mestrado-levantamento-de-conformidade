def cria_no(chave):
  no = dict()

  no["valor"] = chave
  no["esq"] = None
  no["dir"] = None
  no['h'] = 1

  return no


def altura(arvore_):
  return arvore_['h'] if arvore_ else 0


def atualiza_altura_arvore(arvore_):
  if arvore_:
    arvore_['h'] = 1 + max(altura(arvore_["esq"]), altura(arvore_["dir"]))


def rotacao_ll(arvore_):
  nova_raiz = arvore_["esq"]
  arvore_["esq"] = nova_raiz["dir"]
  nova_raiz["dir"] = arvore_

  atualiza_altura_arvore(arvore_)
  atualiza_altura_arvore(nova_raiz)

  return nova_raiz


def rotacao_rr(arvore_):
  nova_raiz = arvore_["dir"]
  arvore_["dir"] = nova_raiz["esq"]
  nova_raiz["esq"] = arvore_

  atualiza_altura_arvore(arvore_)
  atualiza_altura_arvore(nova_raiz)

  return nova_raiz


def fator_balanceamento(arvore_):
  return altura(arvore_["dir"]) - altura(arvore_["esq"]) if arvore_ else 0


def balaceia_arvore(arvore_):
  atualiza_altura_arvore(arvore_)
  fb = fator_balanceamento(arvore_)

  if fb < -1:
    if fator_balanceamento(arvore_["esq"]) <= 0:
      return rotacao_ll(arvore_)
  elif fb > 1:
    if fator_balanceamento(arvore_["dir"]) >= 0:
      return rotacao_rr(arvore_)

  return arvore_


def insere_arvore_binaria(arvore_, chave):
  if not arvore_:
    no = cria_no(chave)
    arvore_ = no    
  elif chave <= arvore_["valor"]:
    arvore_["esq"] = insere_arvore_binaria(arvore_["esq"], chave)
  else:
    arvore_["dir"] = insere_arvore_binaria(arvore_["dir"], chave)

  return balaceia_arvore(arvore_)


def cria_arvore_binaria(chaves_):
  arvore_ = dict()

  for chave in chaves_:
    arvore_ = insere_arvore_binaria(arvore_, chave)

  return arvore_


def percurso_pre_ordem(arvore_):
  if arvore_:
    return f'{arvore_["valor"]} ' + percurso_pre_ordem(arvore_["esq"]) + percurso_pre_ordem(arvore_["dir"])

  return ''
  

def percurso_pos_ordem(arvore_):
  if arvore_:
    return percurso_pos_ordem(arvore_["esq"]) + percurso_pos_ordem(arvore_["dir"]) + f'{arvore_["valor"]} '

  return ''


chaves = eval(input())
i = 1

while chaves:
  arvore = cria_arvore_binaria(chaves)

  pre_ordem = percurso_pre_ordem(arvore).strip()
  pos_ordem = percurso_pos_ordem(arvore).strip()

  print(f"Arvore {i}")
  print(f"pre: {pre_ordem}")
  print(f"pos: {pos_ordem}")
  print()

  chaves = eval(input())
  i += 1
