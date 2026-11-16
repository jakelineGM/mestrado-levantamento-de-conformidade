def imprime_bubble(vetor):
  tam = len(vetor)

  for i in range(tam -1):
    for j in range(tam -1 - i):#
      if vetor[j] > vetor[j+1]:
        print(f"{vetor[j]} <-> {vetor[j+1]}")
        vetor[j], vetor[j+1] = vetor[j+1], vetor[j]

entrada = input().strip()

lista = eval(entrada)

imprime_bubble(lista)

print(lista)
