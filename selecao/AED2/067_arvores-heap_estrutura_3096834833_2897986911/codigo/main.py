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


quaseheap=eval(input())

while (len(quaseheap)>0):
  tam=len(quaseheap)
  max_heapify(quaseheap,0,tam)
  print(quaseheap)

  quaseheap=eval(input())


