def cria_programa(nome, tempo_restante):
  """Cria um dicionário que representa um nó da lista duplamente encadeada, inicialmente
  apontando para None. Você deve ajustar as referências para inserir este nó na lista.
  """
  programa = dict()

  programa['nome'] = nome
  programa['tempo_restante'] = tempo_restante

  programa['ant'] = None
  programa['prox'] = None

  return programa


def cria_lista():
  """Cria um dicionário que representa uma lista circular inicialmente vazia.
  """
  lista = dict()

  lista['prim'] = None
  lista['num_programas'] = 0

  return lista


def insere_fim(lista, programa):
    if lista['prim'] is None:
        lista['prim'] = programa
        programa['prox'] = programa
        programa['ant'] = programa
       # lista['num_programas'] = 1
    else:
        ultimo = lista['prim']['ant']
        ultimo['prox'] = programa
        programa['ant'] = ultimo
        programa['prox'] = lista['prim']
        lista['prim']['ant'] = programa
    lista['num_programas'] += 1
      
def remove(lista, programa):
    if lista['num_programas'] == 0:
        lista['prim'] = None
        lista['num_programas'] == 1
        return None
    else:
        ant = programa['ant']
        prox = programa['prox']

        ant['prox'] = prox
        prox['ant'] = ant

        if lista['prim'] == programa:
            lista['prim'] = prox
        lista['num_programas'] -= 1
        return prox
def main():
  Q, N = map(int, input().split())
  lista = cria_lista()
  
# Lê as configurações do exercício
##cota, num_programas = map(int, input().split(' '))

# Cria uma lista ligada vazia
##lista = cria_lista()

# Lê os programas e os insere na lista
##for _ in range(num_programas):
  for _ in range(N):
      linha = input().split()
      nome = linha[0]
      tempo = int(linha[1])
      programa = cria_programa(nome, tempo)
      insere_fim(lista, programa)
  tempo_atual = 0
  atual = lista['prim']

  while lista['num_programas'] > 0:
      tempo_execucao = min(Q, atual['tempo_restante'])
      atual['tempo_restante'] -= tempo_execucao
      tempo_atual += tempo_execucao

      if atual['tempo_restante'] == 0:
          print(f"{tempo_atual} us: {atual['nome']} finalizou")
          proximo = atual['prox']
          remove(lista, atual)
          if lista['num_programas'] > 0:
              atual = proximo
            
          else:
              break
        
      else:
           atual = atual['prox']
  print(f"{tempo_atual} us: shutdown")
  

if __name__ == "__main__":
    main()
        
      


 ## nome, tempo_total_string = input().split(' ')

  # Cria um nó para o programa
 ## programa = cria_programa(nome, int(tempo_total_string))

  # Insere o programa (nó) no final da lista ligada
  ##insere_fim(lista, programa)


# Agora é com você! Simule a execução de todos os programas, manipulando corretamente
# a lista circular e imprimindo sempre que um programa finaliza sua execução