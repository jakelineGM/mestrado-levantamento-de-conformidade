def PreOrdem(raiz):
    if raiz is not None:
        print(raiz['valor'], end = " ")
        PreOrdem(raiz['esq'])
        PreOrdem(raiz['dir'])

def InOrdem(raiz):
    if raiz is not None:
        InOrdem(raiz['esq'])
        print(raiz['valor'], end = " ")
        InOrdem(raiz['dir'])
      
def PosOrdem(raiz):
    if raiz is not None:
        PosOrdem(raiz["esq"])
        PosOrdem(raiz['dir'])
        print(raiz['valor'], end = " ")
      
arvore = eval(input())
print("Pre-ordem: ", end = " ")
PreOrdem(arvore)
print("\nIn-ordem: ", end = " ")
InOrdem(arvore)
print("\nPos-ordem:", end = " ")
PosOrdem(arvore)