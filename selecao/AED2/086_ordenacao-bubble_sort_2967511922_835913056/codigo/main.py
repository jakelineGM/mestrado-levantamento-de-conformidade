def imprime_bubble(lis):
    n = len(lis)

    for i in range(n, 1, -1):
        trocou = False

        for j in range(1, i):
            print(f"{lis[j-1]} > {lis[j]}?")
  
            if lis[j] < lis[j - 1]:
                lis[j-1], lis[j] = lis[j], lis[j-1]
                trocou = True

        if not trocou:
            return

lis = eval(input() )
imprime_bubble(lis)
print(lis)
      

      
      