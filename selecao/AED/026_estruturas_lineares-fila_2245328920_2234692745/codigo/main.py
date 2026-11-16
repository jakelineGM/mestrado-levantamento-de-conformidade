def calcular_tempo_total(q, tempos):
  fila = list(tempos)
  tempo_total = 0
  
  while fila:
    tempo_atual = fila.pop(0)
    
    if tempo_atual<=q:
      
      tempo_total += tempo_atual
      if fila:
        tempo_total+=q-tempo_atual
    else:
      
      tempo_total+=q
      fila.append(tempo_atual - q)

  return tempo_total


q = int(input().strip())
tempos = list(map(int, input().strip().split()))


resultado = calcular_tempo_total(q, tempos)


print(resultado)