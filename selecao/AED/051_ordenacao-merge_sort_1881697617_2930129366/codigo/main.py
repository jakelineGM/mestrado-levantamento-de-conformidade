import ast

def merge(L,ini, meio, fim):
  i = ini
  j = meio
  aux = []

  while i < meio and j < fim:
    if L[i]<=L[j]:
      aux.append(L[i])
      i += 1
    else:
      aux.append(L[j])
      j += 1

  while i < meio:
    aux.append(L[i])
    i +=1
    
  while j < fim:
    aux.append(L[j])
    j +=1

  L[ini:fim] = aux

def merge_intervalo(L, ini, fim):
  if fim - ini <= 1:
    return

  meio = (ini+fim)//2
  merge_intervalo(L, ini, meio)
  merge_intervalo(L, meio, fim)
  merge(L,ini,meio,fim)

def merge_sort(L):
  merge_intervalo(L,0,len(L))
  
while True:
  linha = input().strip()
  if linha == "[]":
    break
  L = ast.literal_eval(linha)
  merge_sort(L)
  print(L)