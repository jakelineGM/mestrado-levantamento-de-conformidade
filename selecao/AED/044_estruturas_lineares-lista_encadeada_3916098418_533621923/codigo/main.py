def cria_lista_vazia():
    """Cria uma lista vazia. A lista será um dicionário que contém uma referência
    para o primeiro elemento e uma referência para o último elemento (inicialmente
    None), além de um contador do número de nós.
    """
    lista = dict()

    lista['prim'] = None
    lista['fim'] = None
    lista['tamanho'] = 0

    return lista


def insere_em_ordem(lista, valor):
    """Insere um novo elemento no fim da lista. Não se esqueça de ajustar o
    contador do número de elementos.
    """
    novo = dict()
    novo['valor'] = valor
    novo['prox'] = None # continue o código
    if lista['prim'] is None:
       lista['prim'] = novo
       lista['fim'] = novo
    else:
       lista['fim']['prox'] = novo
       lista['fim'] = novo 
    lista['tamanho'] += 1
  
def remove(lista, valor):
    """Procura e remove a primeira ocorrência de um nó que possui o valor
    especificado pelo parâmetro.
    """
    # continue o código
    anterior = None 
    atual = lista['prim']

    while atual is not None:

         if atual['valor'] == valor:
       
           if anterior is None :
              lista['prim'] = atual['prox']
              if lista['prim'] is None :
                 lista['fim'] = None
           else:
        
              anterior['prox'] = atual['prox']
              if atual == lista['fim']:
                   lista['fim'] = anterior
           lista['tamanho'] -= 1
           return
         anterior =atual
         atual = atual['prox']

def imprime(lista):

    elementos = []

    atual = lista['prim']
    while atual is not None:
        elementos.append(str(atual['valor']))
        atual = atual['prox']
    if elementos:
        print(", ".join(elementos) + ".")
    else:
         print(".")              
# Programa principal
lista = cria_lista_vazia()
# Lê os números que precisam ser inseridos na lista
inserir = list(map(int, input().split()))
for i in inserir:
    insere_em_ordem(lista, i)
# Lê os números que devem ser removidos da lista
remover = list(map(int, input().split()))
for r in remover:
    remove(lista, int(r))
# continue o código...
imprime(lista)
if __name__ == "_main_":
    main()