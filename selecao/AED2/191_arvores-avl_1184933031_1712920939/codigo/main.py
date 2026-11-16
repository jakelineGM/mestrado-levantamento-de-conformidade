def altura(no):
  if no is None:
    return 0

  return no['h']

def atualizar_altura(no):
  if no:
    no['h'] = 1 + max(altura(no['esq']), altura(no['dir']))

def fator_balanceamento(no):
  if no is None:
    return 0

  return altura(no['dir']) - altura(no['esq'])

def rotacaoLL(T):
  nova_raiz = T['esq']
  T['esq'] = nova_raiz['dir']
  nova_raiz['dir'] = T
  
  atualizar_altura(T)
  atualizar_altura(nova_raiz)
  
  return nova_raiz

def rotacaoRR(T):
  nova_raiz = T['dir']
  T['dir'] = nova_raiz['esq']
  nova_raiz['esq'] = T

  atualizar_altura(T)
  atualizar_altura(nova_raiz)
  
  return nova_raiz

def inserir(no, chave):
  if no is None:
    return {'valor': chave, 'esq': None, 'dir': None, 'h': 1}

  if chave < no['valor']:
    no['esq'] = inserir(no['esq'], chave)
  else:
    no['dir'] = inserir(no['dir'], chave)
  
  atualizar_altura(no)
  fb = fator_balanceamento(no)

  if fb == -2 and fator_balanceamento(no['esq']) <= 0:
    return rotacaoLL(no)

  if fb == 2 and fator_balanceamento(no['dir']) >= 0:
    return rotacaoRR(no)

  return no  

def pre_ordem(no, resultado):
  if no:
    resultado.append(no['valor'])
    pre_ordem(no['esq'], resultado)
    pre_ordem(no['dir'], resultado)

def pos_ordem(no, resultado):
  if no:
    pos_ordem(no['esq'], resultado)
    pos_ordem(no['dir'], resultado)
    resultado.append(no['valor'])

def main():
  caso = 1
  while True:
    try:
        entrada = input()
        if entrada.strip() == '':
            continue
        chaves = eval(entrada)
        if chaves == []:
          break
        raiz = None
        for chave in chaves:
          raiz = inserir(raiz, chave)

        lista_pre = []
        lista_pos = []
        pre_ordem(raiz, lista_pre)
        pos_ordem(raiz, lista_pos)

        print(f'Arvore {caso}')
        print(f'pre:', ' '.join(map(str, lista_pre)))
        print(f'pos:', ' '.join(map(str, lista_pos)))
        print()

        caso += 1
    except EOFError:
      break

main()    