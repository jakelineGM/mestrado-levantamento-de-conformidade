class Candidato:
  def __init__(self, nome, nota):
    self.nome = nome
    self.nota = nota

entrada = eval(input())
lista_candidatos = []

for elemento in entrada:
  k = Candidato(elemento[0], elemento[1])
  lista_candidatos.append(k)

def pigeonhole_sort(lista):
  espaco_trabalho = []
  candidatos_ordenados = []
  
  for i in range(101):
    espaco_trabalho.append([])

  for candidato in lista:
    chave = int(candidato.nota * 10)
    espaco_trabalho[chave].append(candidato)

  for i in range(100, -1, -1):
    if espaco_trabalho[i] != []:
      for k in espaco_trabalho[i]:
        candidatos_ordenados.append(k)

  return candidatos_ordenados

candidatos = pigeonhole_sort(lista_candidatos)

i = 1
for k in candidatos:
  print(f"{i}. {k.nome} - {k.nota:.1f}")
  i += 1

  
      
  
  
  