
m = int(input())
n = int(input())
h = [None] * m 

for i in range(n):
    k = int(input())
    pos_k = k % m
    i = 0
    while h[(pos_k + i) % m] is not None:
        i += 1
    h[(pos_k + i) % m] = k


for i in range(m):
   if h[i] is not None:
      print("%d: %d" % (i, h[i]))