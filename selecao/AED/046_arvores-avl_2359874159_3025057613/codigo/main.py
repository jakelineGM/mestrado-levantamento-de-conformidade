import ast

def criar_no(valor):
  return{'valor': valor, 'esq':None, 'dir':None, 'h':1}

def altura(no):
  if no is None:
    return 0
  return no['h']
 

def atualiza_altura(no):
  if no is None:
    return 0
  no['h'] = max(altura(no['esq']), altura(no['dir']))+1
  return no['h']
     
def insere_avl(raiz,valor):
  if raiz is None:
     return criar_no(valor)
  if valor <raiz['valor']:
     raiz['esq'] = insere_avl(raiz['esq'],valor)
  else:
    raiz['dir'] = insere_avl(raiz['dir'],valor)
  atualiza_altura(raiz)
  return raiz
def rotacaoLL(T):
  if T is None or T['esq'] is None:
    return T
  nova = T['esq']
  T['esq'] = nova['dir']
  nova['dir'] = T
  atualiza_altura(T)
  atualiza_altura(nova)
  return nova

  

def pre_ordem(no,out):
  if no:
     out.append(str(no['valor']))
     pre_ordem(no['esq'],out)
     pre_ordem(no['dir'],out)
     

def pos_ordem(no,out):
  if no:
     pos_ordem(no['esq'],out)
     pos_ordem(no['dir'],out)
     out.append(str(no['valor']))

def main():
  caso = 1
  while True:
    linha = input().strip()
    if linha == '':
      continue
    lista = ast.literal_eval(linha)
    if lista == []:
      break
    
 
    raiz = None
    for v in lista:
      raiz = insere_avl(raiz, v)
    
    raiz =rotacaoLL(raiz)
 
    pre = []
    pos = []
    
    pre_ordem(raiz, pre)
    pos_ordem(raiz, pos)

    h_raiz = altura(raiz)
    fb = altura(raiz['dir']) - altura(raiz['esq']) if raiz is not None else 0
    
    print(f"Arvore {caso}")
    print(f"h: {h_raiz}")
    print(f"fb: {fb}")
    print("pre:", " ".join(pre))
    print("pos:", " ".join(pos))
    print()
    caso +=1


if __name__ == "__main__":
  main()
  