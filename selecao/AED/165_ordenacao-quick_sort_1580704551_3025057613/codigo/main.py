def partition(teams, low, high, key):
    pivot = teams[high]
    pivot_key = key(pivot)
    i = low - 1

    for j in range(low, high):
        if compare_keys(key(teams[j]), pivot_key) > 0:
            i += 1
            teams[i], teams[j] = teams[j], teams[i]
    teams[i + 1], teams[high] = teams[high], teams[i + 1]
    return i + 1
  

def quick_sort(teams, low, high, key):
    if low < high:
        pi = partition(teams, low, high, key)
        quick_sort(teams, low, pi - 1, key)
        quick_sort(teams, pi + 1, high, key)

def compare_keys(key1, key2):
    for k1, k2 in zip(key1, key2):
        if k1 !=k2:
            if isinstance(k1, int):
                return k1 - k2
            else:
                 return 1 if k1 < k2 else -1
    return 0
  

def main():
    N = int(input(). strip())
    for _ in range(N):
        input()
    # Empty line
        champ_name = input().strip()
        T = int(input().strip())
        teams = {}

        for _ in range(T):
            name = input().strip()
            teams[name]= {"points": 0,"games": 0, "wins": 0, "draws": 0,"losses": 0, "gf": 0,"ga": 0}
        G = int(input().strip())
      
        for _ in range(G):
            line = (input(). strip())
            left, right = line.split("#")
            team1, g1 = left.split(":")
            team2, g2 = right.split(":")
            g1, g2 = int(g1), int(g2)



            teams[team1]["games"] += 1
            teams[team2]["games"] += 1
            teams[team1]["gf"] += g1
            teams[team1]["ga"] += g2
            teams[team2]["gf"] += g2
            teams[team2]["ga"] += g1

  # victoria / default/ nul
            if g1 > g2:
                  teams[team1]["points"] += 3
                  teams[team1]["wins"] += 1
                  teams[team2]["losses"] += 1

            elif g1 < g2:
                  teams[team2]["points"] += 3
                  teams[team2]["wins"] += 1
                  teams[team1]["losses"] += 1

            else:
                teams[team1]["points"] += 1
                teams[team2]["points"] += 1
                teams[team1]["draws"] += 1
                teams[team2]["draws"] += 1

        teams_list = list(teams.items())

        def sort_key(item):
            name, s = item
            return (
                s["points"],
                s["wins"],
                s["gf"] - s["ga"],
                s["gf"],
                -s["games"],  #
                name.lower()  #
              )
        quick_sort(teams_list, 0, len(teams_list) - 1, sort_key)




        print(champ_name)
        for i, (name, s) in enumerate(teams_list, start=1):
            dg = s["gf"] - s["ga"]
            print(f"{i} - {name}: {s['points']} pontos, {s['games']} jogos"
                   f"({s['wins']}-{s['draws']}-{s['losses']}), "
                   f"d.g. {dg} ({s['gf']}-{s['ga']})")
          

        print()


if __name__ == "__main__":
  main()


         






    
      

       

        

  
  

 
      
      


