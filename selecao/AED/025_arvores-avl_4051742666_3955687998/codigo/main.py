def inserir_na_arvore(raiz, valor):
    if raiz is None:
        return {'valor': valor, 'esq': None, 'dir': None}
    elif valor < raiz['valor']:
        raiz['esq'] = inserir_na_arvore(raiz['esq'], valor)
    else:
        raiz['dir'] = inserir_na_arvore(raiz['dir'], valor)
    return raiz

def rotacaoRR(T):
    nova_raiz = T['dir']
    T['dir'] = nova_raiz['esq']
    nova_raiz['esq'] = T
    return nova_raiz

def percurso_pre_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        resultado.append(raiz['valor'])
        percurso_pre_ordem(raiz['esq'], resultado)
        percurso_pre_ordem(raiz['dir'], resultado)
    return resultado

def percurso_pos_ordem(raiz, resultado=None):
    if resultado is None:
        resultado = []
    if raiz is not None:
        percurso_pos_ordem(raiz['esq'], resultado)
        percurso_pos_ordem(raiz['dir'], resultado)
        resultado.append(raiz['valor'])
    return resultado

def processar_arvores(casos_de_teste):
    for i, caso in enumerate(casos_de_teste, start=1):
        if not caso:
            continue
        raiz = None
        for valor in caso:
            raiz = inserir_na_arvore(raiz, valor)
        raiz = rotacaoRR(raiz)
        pre_ordem = percurso_pre_ordem(raiz)
        pos_ordem = percurso_pos_ordem(raiz)
        print(f"Arvore {i}")
        print(f"pre: {' '.join(map(str, pre_ordem))}")
        print(f"pos: {' '.join(map(str, pos_ordem))}")
        print()

# Leitura da entrada
casos_de_teste = []
while True:
    try:
        linha = input()
        if linha == '[]':
            break
        casos_de_teste.append(eval(linha))
    except EOFError:
        break

processar_arvores(casos_de_teste)
