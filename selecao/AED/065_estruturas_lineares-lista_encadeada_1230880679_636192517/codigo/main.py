def tem_tripla(lista):
  if len(lista) < 3:
    return False
  cont = 1
  for i in range(1, len(lista)):
    if lista[i] == lista[i - 1]:
      cont += 1
      if cont >= 3:
        return True
    else:
      cont = 1
  return False


def processar():
  N = int(input().strip())
  for _ in range(N):
    dados = list(map(int, input().split()))

    idx_zero = dados.index(0)
    lista = dados[:idx_zero]
    remover = dados[idx_zero + 1]

    nova_lista = [x for x in lista if x != remover]

    if tem_tripla(nova_lista):
      print("tripla")
    else:
      print("nada")

      
if __name__ == "__main__":
  processar()
 
    
  
