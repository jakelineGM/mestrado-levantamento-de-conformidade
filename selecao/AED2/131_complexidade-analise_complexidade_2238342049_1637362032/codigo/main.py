from math import log2

def bubble_ou_merge(numero_entrada):
  tempo_bubble = (2*numero_entrada**2) - (3*numero_entrada) + 1
  tempo_merge = (6*numero_entrada*log2(numero_entrada)) + (8*numero_entrada) - 6


  if tempo_bubble > tempo_merge:
    print("Usar Merge Sort")
  else:
    print("Usar Bubble Sort")



numero_entrada = eval(input())
bubble_ou_merge(numero_entrada)