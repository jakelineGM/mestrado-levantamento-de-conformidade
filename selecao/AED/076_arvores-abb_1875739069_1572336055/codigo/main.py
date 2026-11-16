class ABB():
  def __init__(self, chave=None):
    self.chave = chave
    self.esq = None
    self.dir = None

  def insert_node(self, no):
    
    if no.chave < self.chave:
      if self.esq is None:
        self.esq = no
      else:
        self.esq.insert_node(no)    
    elif no.chave > self.chave:
      if self.dir is None:
        self.dir = no
      else:
        self.dir.insert_node(no)
    
  def percorre(self, ordem):
    if ordem == 'pre':
      self.visita(self)
    if self.esq is not None:
      self.esq.percorre(ordem)
    if ordem == 'in':
      self.visita(self)
    if self.dir is not None:
      self.dir.percorre(ordem)
    if ordem == 'pos':
      self.visita(self)
      
  def visita(self, no):
    print(f'{no.chave}', end=' ')

valores_arvore = eval(input())
n_arvore = 0

while(valores_arvore != []):
  arvore = ABB(valores_arvore[0])
  for valor in valores_arvore[1:]:
    arvore.insert_node(ABB(int(valor)))

  n_arvore += 1
  print(f'Arvore {n_arvore}')

  print('Pre-ordem: ', end='')
  arvore.percorre('pre')
  print()
  print('In-ordem: ', end='')
  arvore.percorre('in')
  print()
  print('Pos-ordem: ', end='')
  arvore.percorre('pos')
  print()
  print()
  valores_arvore = eval(input())
  