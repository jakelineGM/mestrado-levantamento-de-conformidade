#função para inserir elemento
def insere_hash(num, lista, tam):
  #cálculo do resto
  resto = num % tam;
  #índice do laço abaixo, que vai começar pelo resto definido
  i = resto;

  #percurso da hash. O tamanho é usado diretamente como range, mas 
  for resto in range(tam):
    #O if abaixo avalia se o índice desejado está vazio;
    #Caso esteja, insere o elemento nele mesmo e encerra o laço
    if(lista[i]==None):
      lista[i] = num;
      break;

    #Caso não esteja, pula pro próximo índice
    else:
      if(i==tam): #Caso estejamos no final da tabela, o próximo índice é definido como o 1º.
        i=0;
      else:
        i+=1;
  
  return lista;


#Entrada do tamanho da hash e da quantidade de elementos a serem inseridos
tam = int(input());
elems = int(input());

#Inicia uma lista vazia com o tamanho definido inicialmente;
lista = [None] * tam;
#--> Aprendi a inicialização ""[None] * tamanho" online, então:
#--> Por favor avisar se não for uma prática incorreta na matéria ou inadequada no dia a dia.

#Inserção de elementos na hash
for i in range(elems):
  num = int(input());
  lista = insere_hash(num, lista, tam);

#Impressão da tabela
for i in range(tam):
  if(lista[i] != None):
    print(f"{i}: {lista[i]}");