import sys

def cria_fila_vazia():
    
  fila = dict()

  fila['prim'] = None
  fila['fim'] = None
  fila['tamanho'] = 0

  return fila


def enfileira(fila, valor):
    novo = dict()
    novo['valor'] = valor
    novo['prox'] = None
  
    if fila['tamanho'] == 0 :
      fila['prim'] = novo  
      fila['fim'] = novo
    else:
      fila['fim']['prox'] = novo
      fila['fim'] = novo
  
    fila['tamanho'] += 1  


def desenfileira(fila):
  prim = fila['prim']
  valor = prim['valor']

  fila['prim'] = prim['prox']
  if fila['prim'] is None:
    fila['fim'] = None

  fila['tamanho'] -= 1
  return valor

def main():
  dados = list(map(int, input().split()))
  
  idx = 0
  saida = []

  while idx < len(dados):
    N = dados[idx]
    idx+=1

    if N == 0:
      break

    fila = cria_fila_vazia()

    for carta in range(1,N+1):
      enfileira(fila,carta)
    
    descartadas = []

    while fila['tamanho'] > 1:  
      descartadas.append(desenfileira(fila))
      carta = desenfileira(fila)
      enfileira(fila, carta)

    restou = desenfileira(fila)

    linha_desc = "Descartadas:"
    if descartadas:
      linha_desc += " "+" ".join(str(x) for x in descartadas)

    linha_rest = f"Restou: {restou}"

    saida.append(linha_desc)
    saida.append(linha_rest)
    saida.append("")

  if saida:
    print("\n".join(saida).rstrip())

if __name__ == "__main__":
  main()





  