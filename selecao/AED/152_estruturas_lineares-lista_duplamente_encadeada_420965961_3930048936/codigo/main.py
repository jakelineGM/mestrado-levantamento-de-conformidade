"""/* Estrutura para guardar um elemento da fila.*/"""
def cria_nodo(carta):
  nodo = dict()

  nodo['carta'] = carta
  nodo['prox'] = None

  return nodo

"""/* Estrutura para a fila, que deve ser uma lista ligada. Use uma
 das pontas para representar o início da fila (de onde os
 elementos devem ser retirados) e outra para representar o fim
 da fila (onde os elementos devem ser inseridos).*/"""

def cria_fila():
  fila = dict()

  fila['prim'] = None
  fila['fim'] = None
  fila['tamanho'] = 0

  return fila

"""/* Insere um elemento (carta) na fila. Não se esqueça de atualizar
 o contador de nós para saber facilmente quando resta apenas uma
 carta no monte.*/"""
def insere(fila, carta):
  novo = cria_nodo(carta)

  # A lista está vazia
  if fila['prim'] is None:
    fila['prim'] = novo
    fila['fim'] = novo
  else:
    atual = fila['prim']
    while atual['prox'] is not None:
      atual = atual['prox']

    atual['prox'] = novo
    fila['fim'] = novo
  fila['tamanho'] += 1

"""/* Remove um elemento da fila e retorna o seu valor. Não se esqueça
 * de atualizar o contador.
 */"""
def retira(fila):
  fila_tamanho = tamanho(fila)
  if fila_tamanho >= 2:
    atual = fila['prim']
    carta_descartada = atual['carta']
    # Encontra a penúltima carta do monte
    while atual['prox']['carta'] != fila['fim']['carta']:
      atual = atual['prox']

    # Guarda a segunda carta a ser movida para o fundo
    nova_ultima_carta = fila['prim']['prox']
    # O nó a ser removido não aponta mais para o seu vizinho
    fila['prim']['prox'] = None
    # O nó a direita do nó a ser movido é novo primeiro nó (está no topo)
    fila['prim'] = nova_ultima_carta['prox']
    # A segunda carta não aponta mais para o seu vizinho
    nova_ultima_carta['prox'] = None
    # A antiga última carta aponta para a nova última carta
    fila['fim']['prox'] = nova_ultima_carta
    # O ponteiro 'fim' é atualizado para a nova última carta
    fila['fim'] = nova_ultima_carta
    
    fila['tamanho'] -= 1
    
    return carta_descartada
    
"""/* Retorna o tamanho da fila. Use para saber quantas cartas ainda
 * existem no monte.
 */"""
def tamanho(fila):
  return fila['tamanho']

cartas_numeradas = input().split(' ')
for i in cartas_numeradas:
  if int(i) != 0:
    fila = cria_fila()
    for j in range(1, int(i) + 1):
      insere(fila, j)
    print("Descartadas:", end="")
    for k in range(1, int(i)):
      print("", retira(fila), end="")
    print("\nRestou:", fila['fim']['carta'])
    print()