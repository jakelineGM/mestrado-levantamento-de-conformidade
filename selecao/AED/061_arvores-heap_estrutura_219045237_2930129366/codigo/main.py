import ast

def max_heapify(A, i, n):
  while True:
    esq = 2*i + 1
    dir_ = 2*i + 2
    maior = i

    if esq < n and A[esq] > A[maior]:
      maior = esq
    if dir_ < n and A[dir_] > A[maior]:
      maior = dir_
    if maior == i:
      return
    A[i],A[maior] = A[maior],A[i]
    i = maior

while True:
  linha = input().strip()
  if linha == "[]":
    break
  A = ast.literal_eval(linha)
  if A:
    max_heapify(A,0,len(A))
  print(A)
    