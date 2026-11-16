def imprime_bubble(v):
  n = len(v)
  for i in range(n-1):
    for j in range(n-1-i):
      if v[j] > v[j+1]:
        print(f"{v[j]} <-> {v[j+1]}")
        v[j], v[j+1] = v[j+1], v[j]

v = eval(input())
imprime_bubble(v)

print(v)