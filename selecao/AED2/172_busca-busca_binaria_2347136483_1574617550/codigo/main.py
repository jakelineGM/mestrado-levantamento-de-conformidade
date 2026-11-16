def busca_binaria(v, chave, inicio, fim):
  
  if inicio > fim:
    return -1
  
  meio = ((inicio + fim)//2)

  if v[meio] == chave or (chave < v[meio] and inicio > meio - 1) or (chave > v[meio] and meio + 1 > fim):
    separador = ''
  else:
    separador = ', '

  if isinstance(v[meio], str):
    print(f"'{v[meio]}'", end = separador)
  else:
    print(v[meio], end = separador)
  
  if v[meio] == chave:
    return chave
  else:
    if chave > v[meio]:
      return busca_binaria(v, chave, meio + 1, fim)
    else:
      return busca_binaria(v, chave, inicio, meio - 1)
        
v = eval(input())
vk = eval(input())

for i in range(len(vk)):  
  print("[", end = '')
  busca_binaria(v, vk[i], 0, len(v) - 1)
  print("]", end = '')
  print()
        