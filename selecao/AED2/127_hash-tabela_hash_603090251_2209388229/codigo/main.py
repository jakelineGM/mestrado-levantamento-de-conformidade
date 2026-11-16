def main():

  m = int(input())
  n = int(input())

  table = [None] * m

  for _ in range(n):
    x = int(input())
    res = x % m

    i = 0
    while table[(res+i)% m] is not None:
    
      i+=1
    table[(res+i)%m] = x
    
    
  for i in range(m):
    if table[i] is not None:
      print("%d: %d" % (i, table[i]))
  
main()