def heapify(L,n,i):
  maior = i
  esq = 2 * i + 1
  dir = 2 * i + 2

  if esq < n and L[esq] > L[maior]:
    maior = esq
  if dir < n and L[dir] > L[maior]:
    maior = dir
  if maior != i:
    L[i], L[maior] = L[maior], L[i]
    heapify(L,n,maior)

def heap_sort(L):
  n = len(L)
  for i in range(n//2-1,-1,-1):
    heapify(L,n,i)

  for i in range(n -1,0,-1):
    L[0], L[i] = L[i], L[0]
    heapify(L,i,0)

  return L

def main():
  while True:
    try:
      linha = input().strip()
      if linha == "[]":
       break
      vetor = eval(linha)
      resultado = heap_sort(vetor)
      print(resultado)
    except EOFError:
      break

   # if len(A) > 0:
    #max_heapify(A,0,len(A))

    #print(A)


if __name__ == "__main__":
  main()