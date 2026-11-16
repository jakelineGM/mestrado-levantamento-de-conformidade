def max_heapify(vet,iraiz,tam):
  imaior = iraiz

  filhoesq=2*iraiz+1
  if filhoesq < tam and vet[filhoesq]>vet[imaior]:
    imaior = filhoesq

  filhodir = 2*iraiz+2
  if filhodir < tam and vet[filhodir]>vet[imaior]:
    imaior = filhodir

  if imaior != iraiz:
    #troca
    aux = vet[imaior]
    vet[imaior]= vet[iraiz]
    vet[iraiz]=aux
    max_heapify(vet,imaior,tam)

entrada = eval(input())

while entrada !=[]:
  max_heapify(entrada,0,len(entrada))
  print(entrada)
  print()

  entrada = eval(input())


    
