def countingSort(L):
  menor = min(L)
  maior = max(L)
  intervalo = maior - menor +1

  M = [0] * intervalo

  for i in L:
    M[i-menor] += 1

  acumula=0
  for i in range(0, intervalo):
    for j in range(acumula, acumula+M[i]):    
      L[j] = i + menor
      acumula+= 1

  return (L, M)


entrada = eval(input())

l, m = countingSort(entrada)

print(m)
print(l)