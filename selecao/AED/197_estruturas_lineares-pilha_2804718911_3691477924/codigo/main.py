def cria_nodo(valor):
    """Cria um novo nó contendo o valor a ser inserido na pilha."""
    return {'valor': valor, 'prox': None}

def cria_pilha():
    """Cria uma pilha inicialmente vazia."""
    return {'topo': None, 'tamanho': 0}

def push(pilha, valor):
    """Cria um nó contendo o valor especificado pelo parâmetro e o insere no topo da pilha."""
    novo = cria_nodo(valor)
    novo['prox'] = pilha['topo']
    pilha['topo'] = novo
    pilha['tamanho'] += 1

    return f"push {valor}"

def pop(pilha):
    """Remove um nó do topo da pilha e retorna seu valor."""
    if pilha['topo'] is None:
        return None
    nodo = pilha['topo']
    pilha['topo'] = nodo['prox']
    pilha['tamanho'] -= 1

    return f"pop {nodo['valor']}"

def peek(pilha):
    """Retorna o valor guardado no nó que está no topo da pilha sem modificar a pilha."""
    if pilha['topo'] is None:
        return None
    return pilha['topo']['valor']

def tamanho(pilha):
    """Retorna o número de elementos da pilha."""
    return pilha['tamanho']

def processar_entradas():
    pilha = cria_pilha()
    operacoes = []

    print("Digite os números inteiros, um por linha. Finalize inserindo o número 0.")

    while True:
        entrada = int(input())
        if entrada == 0:
            operacoes.append(push(pilha, entrada))
            break
        operacoes.append(push(pilha, entrada))

        while tamanho(pilha) >= 2 and peek(pilha) < 0:
            topo = pop(pilha)
            operacoes.append(topo)
            segundo = pop(pilha)
            operacoes.append(segundo)
            resultado = int(topo.split()[1]) + int(segundo.split()[1])
            operacoes.append(push(pilha, resultado))

            if resultado == 0:
                for op in operacoes:
                    print(op)
                return

        
        if tamanho(pilha) == 1 and peek(pilha) < 0:
            for op in operacoes:
                print(op)
            return

    for op in operacoes:
        print(op)


processar_entradas()
