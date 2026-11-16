from collections import deque

def simular_terminal():
  Q = int(input().strip())
  temps_estudantes = list(map(int, input().split()))
  file = deque ()
  for temps in temps_estudantes:
      file.append(temps)
  temps_total = 0

  while file:


      temps_necessary = file.popleft()


      if temps_necessary <= Q:

            if temps_necessary == Q or not file:

              temps_total += temps_necessary
            else:

              temps_total += Q  
      else:
            temps_necessary -= Q
            file.append(temps_necessary)
            temps_total +=Q  


  print(temps_total)
if __name__ == "__main__":
    simular_terminal()
        