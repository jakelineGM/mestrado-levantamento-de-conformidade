def imprime_buble(v):

  n = len(v)

  for i in range(n):
    for j in range(0, n - i - 1):
      if(v[j] > v[j+1]):

        print(f"{v[j]} <-> {v[j+1]}")
        v[j] , v[j+1] = v[j+1], v[j]


v = eval(input())

imprime_buble(v)

print(v)