
def percorre_pre(T):
  if T is not None:
    print(T['valor'], end=' ')
    percorre_pre(T['esq'])
    percorre_pre(T['dir'])

def percorre_in(T):
  if T is not None:
    percorre_in(T['esq'])
    print(T['valor'], end=' ')
    percorre_in(T['dir'])

def percorre_pos(T):
  if T is not None:
    percorre_pos(T['esq'])
    percorre_pos(T['dir'])
    print(T['valor'], end=' ')


arvore = eval(input())

print("Pre-ordem: ", end='')
percorre_pre(arvore)

print()

print("In-ordem: ", end='')
percorre_in(arvore)

print()

print("Pos-ordem: ", end='')
percorre_pos(arvore)

print()