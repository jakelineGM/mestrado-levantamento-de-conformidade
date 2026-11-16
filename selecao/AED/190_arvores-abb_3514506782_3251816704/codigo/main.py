def search_bst(tree_root : dict , val : int) -> bool:
  walker = tree_root
  while(walker != None):
    if walker['valor'] == val : return True
    elif val > walker['valor']: 
      #print("Procura a direita")
      walker = walker['dir']
    elif val < walker['valor']: 
      #print("Procura a esquerda")
      walker = walker['esq']
  return False

if __name__ == "__main__":
  tree_root = eval(input())
  while(tree_root):
    hits = 0
    search_vals = eval(input())
    for num in search_vals:
      if(search_bst(tree_root,num)):
        hits+=1
        print(f"Chave {num} encontrada")
      else:
        print(f"Chave {num} nao encontrada")
    print(f"Encontrei {hits} chaves")
    print()
    tree_root = eval(input())
  