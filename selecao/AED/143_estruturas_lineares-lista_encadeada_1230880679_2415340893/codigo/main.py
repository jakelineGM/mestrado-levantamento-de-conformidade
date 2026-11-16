def processa_listas(n, listas):
  resultados = []
  for i in range (n):
    linha = listas[i]
    partes = linha.split(' 0 ')
    lista = list(map(int, partes[0].split()))
    remover = int(partes[1])
    lista = [x for x in lista if x != remover]
    encontrou_tripla = False
    for j in range(len(lista) - 2):
      if lista[j] == lista[j + 1] == lista[j + 2]:      
        encontrou_tripla = True
    if encontrou_tripla:
      resultados.append("tripla")
    else:
      resultados.append("nada")
  return resultados
n = int(input())
listas = [input().strip() for _ in range(n)]
resultados = processa_listas(n, listas)
for resultado in resultados:
  print(resultado)
