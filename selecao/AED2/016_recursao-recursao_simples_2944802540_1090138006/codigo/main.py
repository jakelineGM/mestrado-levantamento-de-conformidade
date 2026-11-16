
def numero_codibentinho(n):
  if n<5:
    return 1
  elif n%17 == 0:
    return 1
    #numerocodibentinho
  elif n%5 == 0:
    if numero_codibentinho(n//5):
      return 1
    else:
      return 0
    #aprovado
  elif n%2==1:
    if numero_codibentinho(n-3):
      return 1
    else:
      return 0
  else:
    return 0

limit = input().split()
j = int(limit[0])
while j<=int(limit[1]):
  if numero_codibentinho(j):
    print(j)
  j = j+1