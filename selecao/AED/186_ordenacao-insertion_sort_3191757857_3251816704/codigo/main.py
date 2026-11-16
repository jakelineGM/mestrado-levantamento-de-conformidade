def insertion_sort(lis):
  print(lis)
  for i in range(1,len(lis)):
    #print(f"Abaixo de {i} deve estar ordenado: {lis}")
    j = i - 1
    aux = lis[i]
    trade = False
    #print(f"Inicializando a busca do local correto de j:{j}")
    while(aux < lis[j] and j  >= 0):
      #print(f"Iterando pela lista aux : {aux} < lis[j] : {lis[j]} j = {j}")
      if(lis[j+1] != lis[j]):
        trade = True
        #print(f"Valores diferentes entre {lis[j+1]} e {lis[j]}")
        lis[j+1] = lis[j]
        print(lis)
      j-=1
    #print(f"Local correto de inserção de {aux} eh: {j+1}")
    lis[j+1] = aux
    if trade:
      print(lis)
        
        

def troca(num1,num2):
  num1,num2 = num2,num1
  return num1,num2


def main():
  lista = eval(input())
  insertion_sort(lista)


if __name__ == "__main__":
  main()