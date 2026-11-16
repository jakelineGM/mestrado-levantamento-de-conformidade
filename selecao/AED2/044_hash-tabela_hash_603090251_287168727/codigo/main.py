def hash():
  tam = int(input()) #leitura das entradas
  quant = int(input())

  tabela = [-1] * tam #inicializacao

  for _ in range(quant): #leitura linha por linha
    k = int(input())

    posicao = k % tam #metodo da divisao

    while tabela[posicao] != -1: #se for != -1 a posicao esta ocupada (sondagem linear)
      posicao = (posicao + 1) % tam

    tabela[posicao] = k #insere na posicao livre 

    for indice in range(tam):
      if tabela[indice] != -1:
        print("%d: %d" % (indice, tabela[indice]))

hash()