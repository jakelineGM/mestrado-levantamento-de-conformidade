def imprime_selection(v):
  tam=len(v)
  for i in range(tam):
    min_idx=i
    for j in range(i+1,tam):
      if(v[j]<v[min_idx]):
        min_idx=j
    v[i], v[min_idx]=v[min_idx], v[i] 
    if (v[i]!=v[min_idx]):
      print(f"{v[min_idx]} <-> {v[i]}")



        
if __name__ =="__main__":
  entrada= input()
  elementos=entrada.strip()[1:-1].split(',')
  lista=[]
  for item in elementos:
    item_limpo=item.strip()
    if item_limpo.startswith("'") and item_limpo.endswith("'"):
      lista.append(item_limpo[1:-1])
    elif item_limpo.startswith(""") and item_limpo.endswith("""):
      lista.append(item_limpo[1:-1])
    else:
      try:
        lista.append(int(item_limpo))
      except ValueError:
        try:
          lista.append(float(item_limpo))
        except ValueError:
          lista.append(item_limpo)
  
imprime_selection(lista)
print(lista)
  