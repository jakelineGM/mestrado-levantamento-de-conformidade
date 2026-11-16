
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
  pilha['topo'] = novo 
  pilha['tamanho'] += 1 

def pop(pilha): 

  if pilha['tamanho'] == 0: 
    return None 

  nodo_removido = pilha['topo'] 
  valor = nodo_removido['valor'] 

  pilha['topo'] = nodo_removido['prox'] 
  pilha['tamanho'] -= 1 

  return valor 

def peek(pilha): 
  if pilha['tamanho'] == 0: 
    return None 
  return pilha['topo']['valor'] 


def tamanho(pilha): 
  return pilha['tamanho'] 

pilha = cria_pilha() 

while True: 
  try: 
    entrada = input() 
    if not entrada: continue 
    numero = int(entrada) 
    push(pilha, numero) 
    print(f"push {numero}") 
    
    parar_execucao = False 
    
    while True: 
      topo = peek(pilha) 
    
      if topo == 0: 
        parar_execucao = True 
        break 
    
      if topo < 0: 
        if tamanho(pilha) >= 2: 
          val1 = pop(pilha) 
          print(f"pop {val1}") 
          
          val2 = pop(pilha) 
          print(f"pop {val2}") 
          
          soma = val1 + val2 
          push(pilha, soma) 
          print(f"push {soma}") 

        else: 
          parar_execucao = True 
          break 
        
      else: 
        break 
    
    if parar_execucao: break 

  except EOFError: 
    break 
  
