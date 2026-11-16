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
  if pilha['topo'] == None:
    pilha['topo'] = novo
  else:
    novo['prox'] = pilha['topo']
    pilha['topo'] = novo
  pilha['tamanho'] += 1
  print("push", valor)
def pop(pilha):
  if pilha['tamanho'] > 0:
    valor = pilha['topo']['valor']
    pilha['topo'] = pilha['topo']['prox']
    pilha['tamanho'] -= 1
    print("pop", valor)
    return valor
def peek(pilha):
  if pilha['topo'] != None:
    return pilha['topo']['valor']
def remove_dois(pilha):
  if pilha['tamanho'] >= 2:
    x = pop(pilha)
    y = pop(pilha)
    push(pilha, x + y)
    return True
  return False
pilha = cria_pilha()
valor = int(input())
while True:
  push(pilha, valor)
  pode_remover = True
  while peek(pilha) < 0:
    if not remove_dois(pilha):
      pode_remover = False
      break
  if not pode_remover or peek(pilha) == 0:
      break
  valor = int(input())
    
  