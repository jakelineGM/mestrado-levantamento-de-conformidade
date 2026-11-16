def inserir_na_arvore_avl(raiz,valor):
  if raiz is None:
    return {'valor': valor, 'esq': None, 'dir':None, 'altura' : 1}
    
  if valor < raiz['valor']:
    raiz['esq'] = inserir_na_arvore_avl(raiz['esq'], valor)
  else: 
    raiz['dir'] = inserir_na_arvore_avl(raiz['dir'], valor)

  raiz['altura'] = 1 + max(altura(raiz['esq']), altura(raiz['dir']))
  
  fator = fator_balanceamento(raiz)

  #Rotação LL
  if fator > 1 and valor < raiz['esq']['valor']:
    return rotacaoRR(raiz, direita = True)
  
  #Rotação RR
  if fator < -1 and valor > raiz['dir']['valor']:
    return rotacaoRR(raiz, direita = False)

  # Rotação LR
  if fator > 1 and valor > raiz['esq']['valor']:
    raiz['esq'] = rotacaoRR(raiz['esq'], direita = False)
    return rotacaoRR(raiz, direita = True)

  #Rotação RL
  if fator < -1 and valor < raiz['dir']['valor']:
    raiz['dir']=rotacaoRR(raiz['dir'], direita = True)
    return rotacaoRR(raiz, direita = False)
    
  return raiz

def altura (no):
  if no is None:
    return 0
  return no.get('altura',0)

def fator_balanceamento(no):
  if no is None:
    return 0
  return altura(no['esq'])- altura(no['dir'])
   
def rotacaoRR(raiz, direita):
  if direita:
    nova_raiz = raiz['esq']
    raiz['esq']= nova_raiz['dir']
    nova_raiz['dir'] = raiz
  else:
    nova_raiz = raiz['dir']
    raiz['dir']= nova_raiz['esq']
    nova_raiz['esq'] = raiz

  raiz['altura'] = 1 + max(altura(raiz['esq']), altura(raiz['dir']))
  nova_raiz['altura'] = 1 + max(altura(nova_raiz['esq']), altura(nova_raiz['dir']))
  return nova_raiz

def pre_ordem(arvore):
  if arvore is None:
    return[]
  return [arvore['valor']] + pre_ordem(arvore['esq']) + pre_ordem(arvore['dir'])           
  
def pos_ordem(arvore):
  if arvore is None:
    return[]
  return pos_ordem(arvore['esq']) + pos_ordem(arvore['dir']) + [arvore['valor']]


# entrada de dados
arvores_input = []
while True:
    arvore_entrada = input().strip()
    if arvore_entrada == '[]':
      break
    elementos = eval(arvore_entrada)
    arvores_input.append(elementos)
print()    

# Processamento
i=0
for arvore_input in arvores_input:
  #inserir na arvore
  arvore = None
  for elemento in arvore_input:
    arvore = inserir_na_arvore_avl(arvore,elemento)

  i +=1 
 
  print (f"Arvore {i}")
  print(f"pre: {' '.join(map(str, pre_ordem(arvore)))}")
  print(f"pos: {' '.join(map(str, pos_ordem(arvore)))}")
  print()