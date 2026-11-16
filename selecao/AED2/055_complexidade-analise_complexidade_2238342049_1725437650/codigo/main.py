from math import log2

def caso_bubble(n):
  n2 = n*n;
  tempo_bubble = 2*n2 - 3*n + 1;
  return tempo_bubble;


def caso_merge(n):
  logn = log2(n);
  tempo_merge = 6*n * logn + 8*n - 6;
  return tempo_merge;

n = int(input());
tempo_bubble = caso_bubble(n);
tempo_merge = caso_merge(n);

if(tempo_bubble > tempo_merge):
  print("Usar Merge Sort");
else:
  print("Usar Bubble Sort");