from math import log2 

n = int(input())
lognum = log2(n)
rnumb = ((2*(n**2))-(3*n)+1)
rnumM = ((6*n)*lognum+(8*n)+6)

if rnumb < rnumM:
  print("Usar Bubble Sort")
else:
  print("Usar Merge Sort")