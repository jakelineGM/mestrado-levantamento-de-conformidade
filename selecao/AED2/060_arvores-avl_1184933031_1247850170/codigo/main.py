import ast 

def altura(no):
  return no['h'] if no else 0

def altura_atual(no):
  no['h'] = 1 + max(altura(no['esq']), altura(no['dir']))

def fator_balanceamento(no):
  return altura(no['dir']) - altura(no['esq'])


def rotacao_esquerda(z):
  y = z['dir']
  T2 = y['esq']

  y['esq'] = z
  z['dir'] = T2

  altura_atual(z)
  altura_atual(y)

  return y

def rotacao_direita(z):
  y = z['esq']
  T3 = y['dir']

  y['dir'] = z
  z['esq'] = T3

  altura_atual(z)
  altura_atual(y)

  return y


def insere(no, chave):
  if not no:
      return {'valor': chave, 'esq': None, 'dir': None, 'h': 1}
  if chave < no['valor']:
    no['esq'] = insere(no['esq'], chave)
  else: 
    no['dir'] = insere(no['dir'], chave)
    
  altura_atual(no)
  fb = fator_balanceamento(no)

  if fb < -1 and chave < no['esq']['valor']:
    return rotacao_direita(no)

  if fb > 1 and chave > no['dir']['valor']:
    return rotacao_esquerda(no)

  return no

def pre_ordem(no, lista):
  if no:
    lista.append(str(no['valor']))
    pre_ordem(no['esq'], lista)
    pre_ordem(no['dir'], lista)

def pos_ordem(no, lista):
  if no:
    pos_ordem(no['esq'], lista)
    pos_ordem(no['dir'], lista)
    lista.append(str(no['valor']))



def main():
  
  num_arvore = 1
  
  while True:
    
    linha = input()
    entrada = ast.literal_eval(linha.strip())
    
    if not entrada:
      break 
    raiz = None
    
    for chave in entrada:
      raiz = insere(raiz, chave)
      
    pre = []
    pos = []
    pre_ordem(raiz, pre)
    pos_ordem(raiz, pos)

    print(f'Arvore {num_arvore}')
    print(f'pre: {" ".join(pre)}')
    print(f'pos: {" ".join(pos)}\n')
    num_arvore += 1

if __name__ == "__main__":
  main()
  
    

  