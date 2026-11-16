def radix_sort(lista):
  divisor = 1

  while divisor <= max(lista):
    baldes = []

    for i in range(10):
      baldes.append([])

    for numero in lista:
      digito = (numero // divisor) % 10
      baldes[digito].append(numero)

    lista = []
    
    for balde in baldes:
      for numero in balde:
        lista.append(numero)

    print(lista)

    divisor *= 10

entrada = eval(input())
radix_sort(entrada)
