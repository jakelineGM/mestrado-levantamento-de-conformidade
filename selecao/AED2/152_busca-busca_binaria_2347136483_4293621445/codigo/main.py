def bb(key, lis, ini, fim, lisRes):

  if ini > fim:
    return lisRes

  pivor = (ini + fim)//2
  lisRes.append(lis[pivor])

  if lis[pivor] == key:
    return lisRes
  elif lis[pivor] > key:
    return bb(key, lis, ini, pivor-1, lisRes)
  else:
    return bb(key, lis, pivor+1, fim, lisRes)


lis = eval(input())
keys = eval(input())

for i in range(0, len(keys)):
  retorno = bb(keys[i], lis, 0, len(lis)-1, [])
  print(f"{retorno}")