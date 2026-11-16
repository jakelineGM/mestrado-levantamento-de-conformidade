def insertion_ou_bubble(numero_entrada):
  tempo_bubble = (2*numero_entrada**2) - (3*numero_entrada) + 1
  tempo_insertion = ((3*numero_entrada**2) + (5*numero_entrada))/2 + 1

  if tempo_bubble > tempo_insertion:
    print("Usar Insertion Sort")
  else:
    print("Usar Bubble Sort")



numero_entrada = eval(input())
insertion_ou_bubble(numero_entrada)