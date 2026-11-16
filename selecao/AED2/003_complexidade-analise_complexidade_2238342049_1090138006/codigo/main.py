from math import log2
passosN = int(input())

bubbleTime = (2*(passosN * passosN) - 3*passosN +1)
mergeTime = (6*passosN*log2(passosN) + 8*passosN-6)


if bubbleTime<mergeTime:
  print("Usar Bubble Sort")
else:
  print("Usar Merge Sort")