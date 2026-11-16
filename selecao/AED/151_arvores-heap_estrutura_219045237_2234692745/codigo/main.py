# def max_heapify(lista, n, i):
#   tam = i
#   esquerda = 2 * i +1
#   direita = 2 * i + 2

#   if esquerda < n and lista[esquerda] > lista[tam]: 
#     tam = esquerda

#   if direita < n and lista[direita] > lista[tam]: 
#     tam = direita

#   if tam != i:
#     temp = lista[i]
#     lista[i] = lista[tam]
#     lista[tam] = temp
#     max_heapify(lista, n, tam)

# todas_entradas = []
# while True: 
#   entrada = input("")
#   entrada_tratada = entrada.strip()
#   if entrada_tratada == "[]":
#     break
  
#   todas_entradas.append(list(map(int, entrada_tratada.strip("[]").split(","))))
# print()
# for enter in todas_entradas:
#   if len(enter) > 1:
#     num = len(enter)
#     max_heapify(enter, num, 0)
#     print(enter)
#   else:
#     print([])

def max_heapify(A, i):
  n = len(A)
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2
  if left < n and A[left] > A[largest]:
    largest = left
    
  if right < n and A[right] > A[largest]:
    largest = right


  if largest != i:
    A[i], A[largest] = A[largest], A[i]
    max_heapify(A, largest)

if __name__ == "__main__":
  listas = []
  while True:
    try:
      entrada = input().strip()
      if entrada == "[]":
        break 
      lista = eval(entrada)
      listas.append(lista)
    except Exception as e:
      print(f"Erro: {e}")
      break 
  print()
  for lista in listas:
    if len(lista)>0:
      max_heapify(lista, 0)
    print(lista)