def cria_lista_vazia():
    lista = dict()

    lista['prim'] = None
    lista['fim'] = None
    lista['tamanho'] = 0

    return lista


def push(lista, valor):
    novo = dict()
    novo['valor'] = valor
    novo['prox'] = None

    if lista['fim'] is not None:
      lista['fim']['prox'] = novo
    else:
      lista['prim'] = novo
    lista['fim'] = novo
    lista['tamanho'] +=1
    return lista
  
def pop(lista):
  aux = None
  if lista['tamanho'] > 0:
    aux = lista['prim']['valor']
    lista['tamanho'] -= 1
    lista['prim'] = lista['prim']['prox']
    if lista['prim'] is None:
      lista['fim'] = None
  return aux

sessao = int(input())
alunos = input().split()
alunos = list(map(int, alunos))
lista = cria_lista_vazia()
tempo = 0
for aluno in alunos:
  push(lista, aluno)
while lista['tamanho'] > 0:
  aluno = pop(lista)
  if aluno > sessao:
    aluno -= sessao
    tempo += sessao
    push(lista, aluno)
  elif lista['tamanho'] == 0:
    tempo += aluno
  else:
    tempo += sessao
print(tempo)