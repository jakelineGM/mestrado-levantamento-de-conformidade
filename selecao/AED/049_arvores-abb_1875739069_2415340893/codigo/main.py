class Nodo:
  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None
class ArvoreBinariaBusca:
  def __init__(self):
    self.raiz = None
  def inserir(self, valor):
    if self.raiz is None:
      self.raiz = Nodo(valor)
    else:
      self._inserir_rec(self.raiz, valor)
  def _inserir_rec(self, nodo, valor):
    if valor < nodo.valor:
      if nodo.esq is None:
        nodo.esq = Nodo(valor)
      else:
        self._inserir_rec(nodo.esq, valor)
    else:
      if nodo.dir is None:
        nodo.dir = Nodo(valor)
      else:
        self._inserir_rec(nodo.dir, valor)
  def pre_ordem(self):
    resultado = []
    self._pre_ordem_rec(self.raiz, resultado)
    return resultado
  def _pre_ordem_rec(self, nodo, resultado):
    if nodo:
      resultado.append(nodo.valor)
      self._pre_ordem_rec(nodo.esq, resultado)
      self._pre_ordem_rec(nodo.dir, resultado)
  def in_ordem(self):
    resultado = []
    self._in_ordem_rec(self.raiz, resultado)
    return resultado
  def _in_ordem_rec(self, nodo, resultado):
    if nodo:
      self._in_ordem_rec(nodo.esq, resultado)
      resultado.append(nodo.valor)
      self._in_ordem_rec(nodo.dir, resultado)
  def pos_ordem(self):
    resultado = []
    self._pos_ordem_rec(self.raiz, resultado)
    return resultado
  def _pos_ordem_rec(self, nodo, resultado):
    if nodo:
      self._pos_ordem_rec(nodo.esq, resultado)
      self._pos_ordem_rec(nodo.dir, resultado)
      resultado.append(nodo.valor)
def processar_arvores():
  contador_arvores = 1
  while True:
    entrada = input().strip()
    if entrada == '[]':
      break
    elementos = eval(entrada)
    arvore = ArvoreBinariaBusca()
    for elemento in elementos:
      arvore.inserir(elemento)
    print(f"Arvore {contador_arvores}")
    print("Pre-ordem:", ' '.join(map(str, arvore.pre_ordem())))
    print("In-ordem:", ' '.join(map(str, arvore.in_ordem())))
    print("Pos-ordem:", ' '.join(map(str, arvore.pos_ordem())))
    print()
    contador_arvores += 1
processar_arvores()













    
      