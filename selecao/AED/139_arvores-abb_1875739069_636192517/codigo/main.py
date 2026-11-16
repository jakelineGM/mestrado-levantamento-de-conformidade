def insere(raiz, valor):
  
  if raiz is None:
    return {'valor': valor, 'esq': None, 'dir': None}
  elif valor < raiz['valor']:
    raiz['esq'] = insere(raiz['esq'], valor)
  else:
    raiz['dir'] = insere(raiz['dir'], valor)
  return raiz

def in_ordem(T, lista):
  
  if T is not None:
    in_ordem(T['esq'], lista)
    lista.append(T['valor'])
    in_ordem(T['dir'], lista)
    
def pre_ordem(T, lista):
  
  if T is not None:
    lista.append(T['valor'])
    pre_ordem(T['esq'], lista)
    pre_ordem(T['dir'], lista)


def pos_ordem(T, lista):
  
  if T is not None:
    pos_ordem(T['esq'], lista)
    pos_ordem(T['dir'], lista)
    lista.append(T['valor'])
    

def main():
  contador = 1
  while True:
    try:
      linha = input().strip()
      if not linha:
        continue
      if linha == '[]':
        break

      
      valores = eval(linha)
      if not valores:
        break

        
      raiz = None
      for v in valores:
        raiz = insere(raiz,v)

      pre, ino, pos = [], [], []

      #resultados 
      pre_ordem(raiz, pre)
      in_ordem(raiz, ino)
      pos_ordem(raiz, pos)

      print(f'Arvore {contador}')
      print('Pre-ordem:', *pre)
      print('In-ordem:', *ino)
      print('Pos-ordem:', *pos)
      print()
    
      contador += 1
      
    except EOFError:
      break


if __name__ == "__main__":
  main()