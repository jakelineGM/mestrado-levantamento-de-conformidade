# peguei da minha 5
def max_heapify(quaseheap,paianalisado,tam):
  indmaior=paianalisado
  filhoesq=2*paianalisado+1
  filhodir=2*paianalisado+2
  if filhoesq<tam and quaseheap[indmaior]<quaseheap[filhoesq]:
    indmaior=filhoesq
  if filhodir<tam and quaseheap[indmaior]<quaseheap[filhodir]:
    indmaior=filhodir

  if indmaior!=paianalisado:
    quaseheap[indmaior],quaseheap[paianalisado]=quaseheap[paianalisado],quaseheap[indmaior]
    max_heapify(quaseheap,indmaior,tam)


def heap_sort(vetor,tam):
  ultimo_pai=tam//2
  for j in range(ultimo_pai,-1,-1):
    max_heapify(vetor,j,tam)
    
  for i in range(tam-1,0,-1):
    vetor[0],vetor[i]=vetor[i],vetor[0]
    max_heapify(vetor,0,i)


vetor= eval(input())
while (len(vetor)>0):
  tam=len(vetor)
  heap_sort(vetor,tam)
  print(vetor)

  vetor= eval(input())