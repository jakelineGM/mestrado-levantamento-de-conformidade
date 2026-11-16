def intercala(l, ini, meio, fim):
  aux = [0] * (fim - ini + 1)
  i = ini
  j = meio + 1
  k = 0

  while i <= meio and j <= fim:
    if l[i] <= l[j]:
      aux[k] = l[i]
      i += 1
    else:
      aux[k] = l[j]
      j += 1
    k += 1

  while i <= meio:
    aux[k] = l[i]
    i += 1
    k += 1

  while j <= fim:
    aux[k] = l[j]
    j += 1
    k += 1

  for k in range(fim - ini + 1):
    l[ini + k] = aux[k]
  
  
def merge(l, ini, fim):
  if ini < fim:
    meio = (ini + fim) // 2
    merge(l, ini, meio)
    merge(l, meio + 1, fim)
    intercala(l, ini, meio, fim)

  
while True:
  l = eval(input())
  if l == []:
    break
  merge(l, 0, len(l) - 1)
  print(l)  