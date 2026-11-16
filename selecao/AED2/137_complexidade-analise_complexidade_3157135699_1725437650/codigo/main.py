def caso_bubble(n):
  n2 = n*n;
  tempo_bubble = 2*n2 - 3*n + 1;
  return tempo_bubble;

def caso_insertion(n):
  n2 = n*n;
  tempo_insertion2 = 3*n2 + 5*n;
  tempo_insertion = tempo_insertion2 / 2
  return tempo_insertion + 1;

n = int(input());
tempo_bubble = caso_bubble(n);
tempo_insertion = caso_insertion(n);

if(tempo_bubble > tempo_insertion):
  print("Usar Insertion Sort");
else:
  print("Usar Bubble Sort");