n = int(input())
m = list()

for k in range(n):
  t = input().split(" ")
  m.append(t)


for l in m:
  aux = list()
  b = l[len(l) - 1]
  c = 1
  
  for i in l:
    if i == '0':
      break
    else:
      if i != b:
        aux.append(i)
  
  for j in range(len(aux) - 1):
    if aux[j] == aux[j + 1]:
      c += 1
      if c == 3:
        print("tripla")
        break
    else:
      c = 1
  
  if c < 3:
    print("nada")
