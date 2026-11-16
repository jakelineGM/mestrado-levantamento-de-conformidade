def busca_binaria(vetor,chave):
  inicio=0
  fim=len(vetor)-1
  vet_busca=[]

  while inicio<=fim:
    meio=(inicio+fim)//2
    vet_busca.append(vetor[meio])
    
    if vetor[meio]==chave:
      break

    if vetor[meio]>chave:
      fim = meio-1

    if vetor[meio]<chave:
      inicio = meio+1

  return vet_busca

vetor=eval(input())
chaves=eval(input())

for chave in chaves:
  print(busca_binaria(vetor,chave))