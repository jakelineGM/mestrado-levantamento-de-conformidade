
def max_heapify(arr):
# arr liste representant le quasi-tas
# i represente indice element  a tester commence par le premier
    n = len(arr)
    i = 0
    while True:
      largest = i
      left = 2 * i + 1
      right = 2 * i + 2
#verifie si l'enfant gauche existe et est plus grand que les parents
      if left < n and arr[left] > arr[largest]:
          largest = left
#verifie si l'enfant droite existe et est plus grand que les parents
      if right < n and arr[right] > arr[largest]:
          largest = right
  # si le plus grand n'est pas le parent,echange et applique recursivement
      if largest != i:
          arr[i], arr [largest] = arr[largest], arr[i]
          i = largest 
      else:
        break
      
import sys
import ast

for line in sys.stdin:
    line = line.strip()
    if not line or line  == '[]':
       continue 
    try:
        arr = ast.literal_eval(line)
        max_heapify(arr)
        print(arr)
    except Exception as e:
           
        print(f"erreur: {e}")


                    

  

             
  