def clean_input(data:str) -> list:
  values = []
  if data != '[]':
    data = data.strip("[]").split(",")
    values = [int(number.strip()) for number in data]
  return values


def search(T: dict, value: int) -> dict:
  if T == None:
    return None

  if int(T['valor']) == value:
    return T

  if value > int(T['valor']):
    return search(T['dir'], value)

  if value < int(T['valor']):
    return search(T['esq'], value)


while True:
  T = eval(input())
  if(T == {}):
    break
  
  values = input()
  values = clean_input(values)

  amount_values = 0

  for value in values:
    found = search(T, value)
    if found is not None:
      amount_values +=1
      print('Chave {} encontrada'.format(found['valor']))
    else:
      print('Chave {} nao encontrada'.format(value))

  print('Encontrei', amount_values, 'chaves')
