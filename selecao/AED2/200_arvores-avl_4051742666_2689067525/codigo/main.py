def rotacaoRR(T):
  direito = arvore["dir"]
  esquerdo = T
  esquerdo["dir"] = None
  filho_esq_do_direito = direito["esq"]
  if filho_esq_do_direito is not None:
    if filho_esq_do_direito["valor"] > esquerdo["valor"]:
      esquerdo["dir"] = filho_esq_do_direito
    else:
      esquerdo["esq"] = filho_esq_do_direito
  T = direito
  T["esq"] = esquerdo
  return T

def imprime_pre_ordem(arvore):
  if arvore is not None:
    print(f"{arvore['valor']} ", end="")
    imprime_pre_ordem(arvore["esq"])
    imprime_pre_ordem(arvore["dir"])

def imprime_pos_ordem(arvore):
  if arvore is not None:
    imprime_pos_ordem(arvore['esq'])
    imprime_pos_ordem(arvore['dir'])
    print(f"{arvore['valor']} ", end="")

def insere(arvore, valor):
  if arvore is None:
    no = cria_no(valor)
    arvore = no
  elif valor > arvore["valor"]:
    arvore["dir"] = insere(arvore["dir"], valor)
  else:
    arvore["esq"] = insere(arvore["esq"], valor)
  return arvore
    
def cria_arvore():
  return None

def cria_no(valor):
  return {'valor': valor, 'esq': None, 'dir': None}

caso = eval(input())
contador = 1

while caso != []:

  arvore = cria_arvore()
  
  for i in range(len(caso)):
    arvore = insere(arvore, caso[i])  

  arvore = rotacaoRR(arvore)
  
  print(f"Arvore {contador}")
  print("pre: ", end="")
  imprime_pre_ordem(arvore)
  print("\npos: ", end="")
  imprime_pos_ordem(arvore)
  print("\n")

  caso = eval(input())
  contador += 1