def countingSort(lis):
  menor = min(lis)
  maior = max(lis)
  tamanhoM = (maior - menor) + 1

  M = [0] * tamanhoM

  for valor in lis:
    M[valor-menor]+=1

  S = []

  for i in range(len(M)):
    for _ in range(M[i]):
      S.append(i+menor)

  return M,S

lis=eval(input())
M,S =countingSort(lis)
print(M)
print(S)
    