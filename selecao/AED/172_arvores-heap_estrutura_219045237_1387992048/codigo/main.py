def max_heapify(lis, n, i):

  maior = i
  esq = (2 * i) + 1
  dir = (2 * i) + 2

  if esq < n and lis[esq] > lis[maior]:
    maior = esq

  if dir < n and lis[dir] > lis[maior]:
    maior = dir

  if maior != i:
    lis[i], lis[maior] = lis[maior], lis[i]
    max_heapify(lis, n, maior)

def main():
  while True:
    try:
      linha = input().strip()
      if linha == "[]":
        break
      
      lis = eval(linha)
      if not lis:
        continue

      n = len(lis)
      
      max_heapify(lis, n, 0)
      print(lis)
    except EOFError:
      break

if __name__ == "__main__":
  main()