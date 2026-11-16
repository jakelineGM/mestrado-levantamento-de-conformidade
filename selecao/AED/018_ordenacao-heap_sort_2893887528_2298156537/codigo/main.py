import ast 
def esquerda(i):
  return 2*i+1
def direita(i):
  return 2*i+2
def max_heapfy(A,i,heap_size):
  e=esquerda(i)
  d=direita(i)
  maior=i
  if e < heap_size and A[e] > A[maior]:
    maior=e
  if d < heap_size and A[d] > A[maior]:
    maior=d
  if maior!= i:
    A[i],A[maior]= A[maior],A[i]
    max_heapfy(A,maior, heap_size)
def lado_max_heap(A):
  heap_size = len(A)
  for i in range(len(A)//2-1,-1,-1):
    max_heapfy(A,i,heap_size)
def heap_sort(L):
  heap_size=len(L)
  lado_max_heap(L)
  for i in range(len(L)-1,0,-1):
    L[0],L[i]= L[i],L[0]
    heap_size-=1
    max_heapfy(L,0,heap_size)



if __name__ =="__main__":
  while True:  
    entrada= input()
    elementos=entrada.strip()[1:-1].split(',')
    lista=[]
    for item in elementos:
      item_limpo=item.strip()
      if item_limpo.startswith("'") and item_limpo.endswith("'"):
        lista.append(item_limpo[1:-1])
      elif item_limpo.startswith(""") and item_limpo.endswith("""):
        lista.append(item_limpo[1:-1])
      else:
        try:
          lista.append(int(item_limpo))
        except ValueError:
          try:
            lista.append(float(item_limpo))
          except ValueError:
            lista.append(item_limpo)
    if entrada == "[]":
      break
    lista = ast.literal_eval(entrada)
    heap_sort(lista)
    print(lista)