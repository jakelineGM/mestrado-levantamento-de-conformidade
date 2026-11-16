def insertion(x):
  print(x)
  for i in range(1,len(x)):
    chave = x[i]
    j = i-1
    while j>=0 and chave < x[j]:
      if x[j+1]!=x[j]:
        x[j+1] = x[j]
        print(x)
      j-=1
    if x[j+1]!=chave:
      x[j+1]=chave
      print(x)



insertion(eval(input()))