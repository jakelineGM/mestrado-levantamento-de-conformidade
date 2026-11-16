def bubble(x):
  for i in range(len(x)-1):
    troca = False
    for j in range(len(x)-i-1):
      if x[j]>x[j+1]:
        print(x[j],"<->",x[j+1])
        x[j],x[j+1] = x[j+1],x[j]
        troca = True
    if not troca:
      break
  return x
print(bubble(eval(input())))