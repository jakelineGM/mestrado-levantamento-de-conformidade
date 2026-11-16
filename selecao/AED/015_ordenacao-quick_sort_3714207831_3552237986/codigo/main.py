import math

def quick_sort(vet: list):
  if len(vet) > 1:
    partition_point = partition(vet)
    left = quick_sort(vet[:partition_point])
    right = quick_sort(vet[partition_point:])
    vet = left + right

  return vet
    

def partition(vet: list):
  pivot = vet[math.ceil(len(vet) / 2)]
  i = 0
  j = len(vet) - 1
  while True:
    while vet[i] < pivot: i += 1
    while vet[j] > pivot: j -= 1
    if i < j:
      vet[i], vet[j] = vet[j], vet[i]
    else:
      return j

while True:
  vet = eval(input())
  if not vet:
    exit()

  print(quick_sort(vet))