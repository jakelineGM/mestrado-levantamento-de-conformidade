def max_heapify(v):
  n = len(v)
  i=0
  while True:
    l = 2 * i + 1
    r = 2 * i + 2
    largest = i

    if l < n and v[l] > v[largest]:
      largest = l
    if r < n and v[r] > v[largest]:
      largest = r

    if largest != i:
      v[i], v[largest] = v[largest], v[i]
      i = largest

    else: 
      break 

def main():
  while True: 
    try:
      linha = input().strip()
    except EOFError:
      break

    if not linha:
      continue
    v = eval(linha)
    if v == []:
      break

    max_heapify(v)
    print(v)

if __name__ == "__main__":
  main()