import sys

def cria_fila_vazia():
    """Cria uma lista vazia. A lista será um dicionário que contém uma referência
    para o primeiro elemento e uma referência para o último elemento (inicialmente
    None), além de um contador do número de nós.
    """
    fila = dict()

    fila['prim'] = None
    fila['fim'] = None
    fila['tamanho'] = 0

    return fila


def insere_fim(fila, valor):
    """Insere um novo elemento no fim da lista. Não se esqueça de ajustar o
    contador do número de elementos.
    """
    novo = dict()
    novo['valor'] = valor
    novo['prox'] = None

    if fila["prim"] is None:
        fila["prim"] = novo
        fila["fim"] = novo
    else:
        fila["fim"]["prox"] = novo
        fila["fim"] = novo

    fila["tamanho"] += 1


def remove(fila):
    if fila["prim"] is None:
        return

    primeiro = fila["prim"]
    valor = primeiro["valor"]

    fila["prim"] = primeiro["prox"]
    if fila["prim"] is None:
        fila["fim"] = None

    fila["tamanho"] -= 1
    return valor

def tamanho(fila):
    return fila["tamanho"]


def simula():
    entrada = sys.stdin.readline().split(" ")
    idx = 0
  
    while idx < len(entrada):
        n = int(entrada[idx])
        idx+=1

        if n == 0:
            break

        fila = cria_fila_vazia()
        for i in range(1, n+1):
            insere_fim(fila, i)

        descartadas = []
        while tamanho(fila) >= 2:
            corta = remove(fila)
            descartadas.append(corta)

            fundo = remove(fila)
            insere_fim(fila, fundo)
      
        str_descartadas = " ".join(map(str, descartadas))
        print(f"Descartadas: {str_descartadas}")

        restante = remove(fila)
        print(f"Restou: {restante}")
        print()

simula()

  