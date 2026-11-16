def inserir(raiz, chave):
  if raiz is None:
    return {'valor': chave, 'esq': None, 'dir': None}
  if chave < raiz['valor']:
    raiz['esq'] = inserir(raiz['esq'], chave)
  else:
    raiz['dir'] = inserir(raiz['dir'], chave)
  return raiz

def encontrar_maximo(raiz):
  while raiz['dir'] is not None:
    raiz = raiz['dir']
  return raiz['valor']

def encontrar_minimo(raiz):
  while raiz['esq'] is not None:
    raiz = raiz['esq']
  return raiz['valor']

def encontrar_antecessor_sucessor(raiz, chave):
  antecessor = None
  sucessor = None
  
  while raiz is not None and raiz['valor']  != chave:
    if chave < raiz['valor']:
      sucessor = raiz['valor']
      raiz = raiz['esq']
    else:
      antecessor = raiz['valor']
      raiz = raiz['dir']
      
  if raiz is None:
    return None, None
  
  antecessor = encontrar_maximo(raiz['esq'])
  sucessor = encontrar_minimo(raiz['dir'])

  return antecessor, sucessor

valores = eval(input())
consultas = eval(input())

raiz = None
for chave in valores:
  raiz = inserir(raiz, chave)

for chave in consultas:
  antecessor, sucessor = encontrar_antecessor_sucessor(raiz, chave)
  print(f"Chave {chave} tem antecessor {antecessor} e sucessor {sucessor}")
                        