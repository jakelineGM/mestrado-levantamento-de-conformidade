def busca_binaria(lis,chaves):

  for chave in chaves:
    lis_verificada = []
    inicio = 0
    fim = len(lis)-1
    meio = (inicio+fim)//2
    while inicio <= fim:
      lis_verificada.append(lis[meio])
      if chave < lis[meio]:
        fim = meio - 1
        meio = (inicio + fim)//2
      elif chave > lis[meio]:
        inicio = meio+1
        meio = (inicio+fim)//2     
      else:
        break
    print(lis_verificada[:])
    
     
          




  
lis = eval(input())
chaves = eval(input())
busca_binaria(lis,chaves)