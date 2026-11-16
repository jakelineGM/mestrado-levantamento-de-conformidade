def numero_de_codibentinho(num):
  if num < 5:
    return True
  elif num % 17 == 0:
    return True
  elif (num % 5 == 0) and (num % 17 != 0) and numero_de_codibentinho(num/5):
    return True
  elif (num % 2 != 0) and (num % 5 != 0) and (num % 17 != 0) and numero_de_codibentinho(num-3):
    return True
  else:
    return False

n, m = map(int, input().split())

for i in range(n, m+1):
  if numero_de_codibentinho(i):
    print(i)
