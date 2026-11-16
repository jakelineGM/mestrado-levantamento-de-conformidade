def max_heapify(v, i):
  
  if len(v) != 0:

    esq = (2*i)+1
    dir = (2*i)+2

    no_esq = None
    no_dir = None
    
    if esq < len(v):
      no_esq = v[esq]

    if dir < len(v):
      no_dir = v[dir]

    if v[i] > v[(i-1)//2] and i!=0:
      temp = v[(i-1)//2]
      v[(i-1)//2] = v[i]
      v[i] = temp
      
    if no_esq:
      if no_dir:
        if v[esq]>=v[dir]:
          max_heapify(v, esq)
          max_heapify(v, dir)
      else:
        max_heapify(v, esq)
    
    if no_dir:
      if no_esq:
        if v[dir]>=v[esq]:
          max_heapify(v, dir)
          max_heapify(v, esq)
      else:
        max_heapify(v, dir)

v = eval(input())

results = []
while (v!= []):

  max_heapify(v, 0)
  
  results.append(v)
  v = eval(input())

for line in results: 
  print(line)




