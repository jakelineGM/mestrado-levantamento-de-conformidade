
def intercalacao(lisA, lisB):
  lisC = []
  i=0
  j=0

  while i < len(lisA) or j < len(lisB):

    if i == len(lisA):
      lisC.append(lisB[j])
      j+=1
    elif j == len(lisB):
      lisC.append(lisA[i])
      i+=1  
    elif lisA[i]<=lisB[j]:
        lisC.append(lisA[i])
        i+=1
    else:
        lisC.append(lisB[j])
        j+=1 
  
  return lisC


lisA = eval(input())
lisB = eval(input())
print(intercalacao(lisA, lisB))