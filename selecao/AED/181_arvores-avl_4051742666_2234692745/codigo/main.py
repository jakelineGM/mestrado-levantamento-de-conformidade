class No:
  def __init__(self, valor):
    self.valor = valor
    self.esq = None
    self.dir = None

def inserir(raiz, valor):
  if raiz is None:
    return No(valor)
  if valor < raiz.valor:
    raiz.esq = inserir(raiz.esq, valor)
  else:
    raiz.dir = inserir(raiz.dir, valor)
  return raiz

def pre_ordem(raiz, resultado):
  if raiz is not None:
    resultado.append(str(raiz.valor))
    pre_ordem(raiz.esq, resultado)
    pre_ordem(raiz.dir, resultado)

def in_ordem(raiz, resultado):
  if raiz is not None:
    in_ordem(raiz.esq, resultado)
    resultado.append(str(raiz.valor))
    in_ordem(raiz.dir, resultado)

def pos_ordem(raiz, resultado):
  if raiz is not None:
    pos_ordem(raiz.esq, resultado)
    pos_ordem(raiz.dir, resultado)
    resultado.append(str(raiz.valor))

def rotacaoRR(raiz):
  if raiz is None or raiz.dir is None:
    return raiz
  nova_raiz = raiz.dir
  raiz.dir = nova_raiz.esq
  nova_raiz.esq = raiz
  return nova_raiz

# def processa_arvores():
#   entradas = []

#   while True:
#     entrada = input().strip()
#     if entrada == '[]':
#       break 
#     entradas.append(eval(entrada))
#     print()
#     contador = 1
#     for elementos in entradas:
#       raiz = None
      
#       for elemento in elementos:
#         raiz = inserir(raiz, elemento)
        
#       raiz = rotacaoRR(raiz)
      
#       if contador > 1:
#         print()
#       print(f"Arvore {contador}")
      
#       resultado_pre = []
#       pre_ordem(raiz, resultado_pre)
#       print("pre:", " ".join(resultado_pre))
      
#       resultado_pos = []
#       pos_ordem(raiz, resultado_pos)
#       print("pos:", " ".join(resultado_pos))
      
#       contador+=1

def processa_arvores():
  entradas = []
  while True:
    entrada = input().strip()
    if entrada == '[]':
      break 
    entradas.append(eval(entrada))
  contador = 1
  print()
  for elementos in entradas:
    raiz = None
    for elemento in elementos:
      raiz = inserir(raiz, elemento)
    raiz = rotacaoRR(raiz)
    if contador > 1:
      print()
    print(f"Arvore {contador}")
    
    resultado_pre = []
    pre_ordem(raiz, resultado_pre)
    print("pre:", " ".join(resultado_pre))
    
    resultado_pos = []
    pos_ordem(raiz, resultado_pos)
    print("pos:", " ".join(resultado_pos))
    
    contador+=1

if __name__ == "__main__":
  processa_arvores()
  