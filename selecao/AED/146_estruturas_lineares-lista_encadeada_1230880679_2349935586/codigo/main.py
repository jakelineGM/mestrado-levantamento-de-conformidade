def verificar_triplas():
  # Lê o número de listas a serem processadas
  try:
    n = int(input())
  except (ValueError, EOFError):
    return

  # Lista para guardar as respostas
  resultados = []
  
  for _ in range(n):
    # Lê a linha inteira contendo a lista + sentinela + número a remover
    linha = list(map(int, input().split()))

    # Encontra a posição do sentinela (0)
    try:
      indice_zero = linha.index(0)
    except ValueError:
      # Caso de segurança se não houver 0
      print("nada")
      continue

    # Separa a lista original e o alvo a ser removido
    # Tudo antes do 0 é a lista
    lista_original = linha[:indice_zero]
    # O número logo após o 0 é o alvo
    alvo = linha[indice_zero + 1]

    # Cria uma nova lista contendo apenas os elementos diferentes
    lista_limpa = [num for num in lista_original if num != alvo]

    # Verifica se há triplas consecutivas
    encontrou_tripa = False

    # Só é possível ter tripla se a lista tiver pelo menos 3 elementos
    if len(lista_limpa) >= 3:
      for i in range(len(lista_limpa) - 2):
        # Checa se o elemento atual, o próximo e o seguinte são iguais
        if lista_limpa[i] == lista_limpa[i+1] == lista_limpa[i+2]:
          encontrou_tripa = True
          break

    if encontrou_tripa:
      resultados.append("tripla")
    else:
      resultados.append("nada")

  for res in resultados:
    print(res)

verificar_triplas()        