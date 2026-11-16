from collections import deque

def simuler_terminal():
  #lecture de Q
    Q = int(input().strip())
  #lecture du temps necessaire pour chaque etudiant
    temps_etudiants = list(map(int, input().split()))
  #creation de la file avec le temps restant pour chaque etudiant.
    file = deque ()
    for temps in temps_etudiants:
        file.append(temps)
    temps_total = 0
  # simulation jusqu'a ce que tous les etudients aient terminees
    while file:
    #recuperer le premier etudiant de la file
         
         
        temps_necessaire = file.popleft()
     
      
    #l'etudiant utilise le terminal
        if temps_necessaire <= Q:
      # il termine son travail
            if temps_necessaire == Q or not file:
      # si termine exactement a Q ou c'est le dernier etudiant
               temps_total += temps_necessaire
            else:
              # terminer avant Q mais il ya  d'autre etudiant
              # terminal reste occupe Q munite
                temps_total += Q
        else:  
          # il n'a pas termine,utilise Q munite et retourne en file
            temps_necessaire -= Q
            file.append(temps_necessaire)
            temps_total += Q
              
    # affiche du resultat
    print(temps_total)
    # execution de la simulation
if __name__ == "__main__":
      simuler_terminal()