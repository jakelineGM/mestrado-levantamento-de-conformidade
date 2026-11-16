import sys

class Node:
    def __init__(self, valor):
      self.valor = valor
      self.esq = None
      self.dir = None


def inserir(raiz,valor):
     if raiz is None:
       return Node(valor)
     if valor < raiz.valor:
       raiz.esq = inserir(raiz.esq, valor)
     else:
       raiz.dir = inserir(raiz.dir, valor)
     return raiz
    

def pre_ordem(node, resultado):
      if node:
        resultado.append(str(node.valor))
        pre_ordem(node.esq, resultado)
        pre_ordem(node.dir, resultado)
     
def in_ordem(node, resultado):
      if node:
        in_ordem(node.esq, resultado)
        resultado.append(str(node.valor))
        in_ordem(node.dir, resultado)
    
    
       
         
def pos_ordem(node, resultado):
      if node:
        pos_ordem(node.esq, resultado)
        pos_ordem(node.dir, resultado)
        resultado.append(str(node.valor))



def main():
    count = 1
    while True:
      entrada = eval(input().strip())
      if entrada == []:
        break 
      raiz = None
      for v in entrada:
        raiz = inserir(raiz,v)

      pre = []
      in_ = []
      pos = []
      pre_ordem(raiz,pre)
      
      in_ordem(raiz,in_)
      pos_ordem(raiz,pos)
  
      
        
      # Print results
      print(f"Arvore {count}")
      print("Pre-ordem:", " ".join(pre))
      print("In-ordem:", " ".join(in_))
      print("Pos-ordem:", " ".join(pos))
      print()
      count+=1
      
if __name__ == "__main__":
   main()