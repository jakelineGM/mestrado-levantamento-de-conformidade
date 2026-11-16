import sys

# Estrutura para guardar um elemento da fila.
def cria_nodo(carta):
  nodo = {
    "carta": carta,
    "prox": None,
  }
  return nodo

# Estrutura para a fila, que deve ser uma lista ligada. Use uma
# das pontas para representar o início da fila (de onde os
# elementos devem ser retirados) e outra para representar o fim
# da fila (onde os elementos devem ser inseridos).
def cria_fila():
  fila = {
    "prim": None,
    "fim": None,
    "tamanho": 0,
  }
  return fila

# Insere um elemento (carta) na fila. Não se esqueça de atualizar
# o contador de nós para saber facilmente quando resta apenas uma
# carta no monte.

def insere(fila, carta):
  novo = cria_nodo(carta)
  
  if fila["prim"] is None:
    fila["prim"] = novo
    fila["fim"]  = novo
  else:
    fila["fim"]["prox"] = novo
    fila["fim"] = novo

  fila["tamanho"] += 1

# Remove um elemento da fila e retorna o seu valor.

def retira(fila):
  if fila["prim"] is None:
    return None

  removido = fila["prim"]
  valor = removido["carta"]

  fila["prim"] = removido["prox"]
  if fila["prim"] is None:
    fila["fim"] = None

  fila["tamanho"] -= 1
  return valor

# Retorna o tamanho da fila. Use para saber quantas cartas ainda
# existem no monte.

def tamanho(fila):
  return fila["tamanho"]

def main():
  linha = input().strip()
  if not linha:
    return
  
  ns = list(map(int, linha.split()))
  
  for N in ns:
    if N == 0:
      break

    fila = cria_fila()

    for i in range(1, N + 1):
      insere(fila, i)

    descartadas = []

    while tamanho(fila) > 1:
      descartadas.append(retira(fila))

      proxima = retira(fila)
      insere(fila, proxima)

    restou = retira(fila)

    if descartadas:
      print("Descartadas:", " ".join(str(x) for x in descartadas))
    else:
      print("Descartadas:")

    print(f"Restou: {restou}")
    print()


if __name__ == "__main__":
  main()