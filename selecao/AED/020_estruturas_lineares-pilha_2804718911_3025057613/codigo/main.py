def cria_nodo(valor):
  nodo = dict()
  nodo['valor'] = valor
  nodo['prox'] = None
  return nodo

def cria_pilha():
  pilha = dict()
  pilha['topo'] = None
  pilha['tamanho'] = 0
  return pilha


def push(pilha, valor):
 
    novo = cria_nodo(valor)
    novo['prox'] = pilha['topo']
    pilha['topo']= novo
    pilha['tamanho'] += 1
    print(f"push {valor}")
    return valor
  
  # Insira o novo nó na pilha...


def pop(pilha):
    if pilha['topo'] is None:
       return None
    valor = pilha['topo']['valor']
    pilha['topo']= pilha['topo']['prox']
    pilha['tamanho'] -= 1
    print(f"pop {valor}")
    return valor

def peek(pilha):

  if pilha['topo'] is None:
      return None
  return pilha['topo']['valor']


def tamanho(pilha):
    
      return pilha['tamanho']

def processa_sequencia():
    pilha = cria_pilha()
    try:
        while True:
            line = input()
            if line.strip() == '':
                continue
            num = int(line.strip())

            push(pilha, num)
            topo = peek(pilha)
            if topo ==0:
                return


            while tamanho(pilha) >=2:
              topo = peek(pilha)
              if topo is None or topo >= 0:
                  break
              a = pop(pilha)
              b = pop(pilha)
              if a is not None and b is not None:
                  soma = a + b
                  push(pilha, soma)
                  if peek(pilha) ==0:
                    return
                  topo = peek(pilha)
                  if tamanho(pilha) < 2 and topo is not None and topo < 0:
                    return

    except EOFError:
        pass
if __name__ == "__main__":
    processa_sequencia()
  


#def tamanho(pilha):
#  """Retorna o número de elementos da pilha. Use para saber se a pilha
 # contém elementos suficientes para remover dois de uma vez só.
  #"""
  #return pilha['tamanho']