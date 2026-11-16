def obter_altura_no(no_atual):
    if no_atual is None:
        return 0
    return no_atual['h']


def recalcular_altura_no(no_atual):
    if no_atual is not None:
        altura_subarvore_esquerda = obter_altura_no(no_atual['esq'])
        altura_subarvore_direita = obter_altura_no(no_atual['dir'])
        no_atual['h'] = max(
            altura_subarvore_esquerda,
            altura_subarvore_direita
        ) + 1


def calcular_fator_balanceamento(no_atual):
    return obter_altura_no(no_atual['dir']) - obter_altura_no(no_atual['esq'])


def executar_rotacao_direita(raiz_subarvore):
    nova_raiz_subarvore = raiz_subarvore['esq']
    subarvore_reposicionada = nova_raiz_subarvore['dir']

    nova_raiz_subarvore['dir'] = raiz_subarvore
    raiz_subarvore['esq'] = subarvore_reposicionada

    recalcular_altura_no(raiz_subarvore)
    recalcular_altura_no(nova_raiz_subarvore)

    return nova_raiz_subarvore


def executar_rotacao_esquerda(raiz_subarvore):
    nova_raiz_subarvore = raiz_subarvore['dir']
    subarvore_reposicionada = nova_raiz_subarvore['esq']

    nova_raiz_subarvore['esq'] = raiz_subarvore
    raiz_subarvore['dir'] = subarvore_reposicionada

    recalcular_altura_no(raiz_subarvore)
    recalcular_altura_no(nova_raiz_subarvore)

    return nova_raiz_subarvore


def inserir_valor_avl(no_corrente, valor_inserido):
    if no_corrente is None:
        return {
            'valor': valor_inserido,
            'esq': None,
            'dir': None,
            'h': 1
        }

    if valor_inserido < no_corrente['valor']:
        no_corrente['esq'] = inserir_valor_avl(
            no_corrente['esq'],
            valor_inserido
        )
    else:
        no_corrente['dir'] = inserir_valor_avl(
            no_corrente['dir'],
            valor_inserido
        )

    recalcular_altura_no(no_corrente)
    fator = calcular_fator_balanceamento(no_corrente)

    # Caso LL
    if fator < -1 and valor_inserido < no_corrente['esq']['valor']:
        return executar_rotacao_direita(no_corrente)

    # Caso RR
    if fator > 1 and valor_inserido > no_corrente['dir']['valor']:
        return executar_rotacao_esquerda(no_corrente)

    # Caso LR
    if fator < -1 and valor_inserido > no_corrente['esq']['valor']:
        no_corrente['esq'] = executar_rotacao_esquerda(no_corrente['esq'])
        return executar_rotacao_direita(no_corrente)

    # Caso RL
    if fator > 1 and valor_inserido < no_corrente['dir']['valor']:
        no_corrente['dir'] = executar_rotacao_direita(no_corrente['dir'])
        return executar_rotacao_esquerda(no_corrente)

    return no_corrente


def percorrer_pre_ordem(no_corrente, lista_resultado):
    if no_corrente is not None:
        lista_resultado.append(no_corrente['valor'])
        percorrer_pre_ordem(no_corrente['esq'], lista_resultado)
        percorrer_pre_ordem(no_corrente['dir'], lista_resultado)


def percorrer_pos_ordem(no_corrente, lista_resultado):
    if no_corrente is not None:
        percorrer_pos_ordem(no_corrente['esq'], lista_resultado)
        percorrer_pos_ordem(no_corrente['dir'], lista_resultado)
        lista_resultado.append(no_corrente['valor'])


contador_casos = 1

while True:
    entrada_usuario = input().strip()
    lista_valores = eval(entrada_usuario)

    if len(lista_valores) == 0:
        break

    raiz_principal = None

    for valor in lista_valores:
        raiz_principal = inserir_valor_avl(raiz_principal, valor)

    resultado_pre_ordem = []
    resultado_pos_ordem = []

    percorrer_pre_ordem(raiz_principal, resultado_pre_ordem)
    percorrer_pos_ordem(raiz_principal, resultado_pos_ordem)

    print(f"Arvore {contador_casos}")
    print("pre:", " ".join(map(str, resultado_pre_ordem)))
    print("pos:", " ".join(map(str, resultado_pos_ordem)))
    print()

    contador_casos += 1

