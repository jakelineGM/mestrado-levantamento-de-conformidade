def bubble(arr):
  trocou = True
  it = 0
  while trocou:
    trocou = False
    for i in range(1, len(arr) - it):
      if(arr[i-1] > arr[i]):
        trocou = True
        print(arr[i-1], "<->", arr[i])
        arr[i-1], arr[i] = arr[i], arr[i-1]
    it+=1
  return arr

print(bubble(eval(input())))

