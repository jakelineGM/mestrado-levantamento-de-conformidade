def max_heapify(vet: list, root: int):
  largest = root
  left_child = 2 * root + 1
  if left_child < len(vet) and vet[left_child] > vet[largest]:
    largest = left_child
  right_child = 2 * root + 2
  if right_child < len(vet) and vet[right_child] > vet[largest]:
    largest = right_child

  if largest != root:
    vet[root], vet[largest] = vet[largest], vet[root]
    max_heapify(vet, largest)


while True:
  vet = eval(input())
  if not vet:
    exit()
  last = len(vet) // 2 - 1
  for i in range(last, -1, -1):
    max_heapify(vet, i)
  print(vet)
    
    