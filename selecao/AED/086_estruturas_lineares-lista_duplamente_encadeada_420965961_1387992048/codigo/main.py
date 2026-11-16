from collections import deque

def card_game_simulation(inputs):
  results = []

  for n in inputs:
    if n ==0:
      break

    queue = deque(range(1, n+1))
    discarded = []
    
    while len(queue) > 1:
      discarded.append(queue.popleft())
      queue.append(queue.popleft())

    remaing = queue.pop()

    discarded_str = " ".join(map(str, discarded))
    results.append(f"Descartadas: {discarded_str}\nRestou: {remaing}\n")

  return "\n".join(results)

inputs = []
while True:
  entrada = input()
  numeros = list(map(int,entrada.split()))
  inputs.extend(numeros)
  if 0 in numeros:
    break

cases = []
current_case = []
  
for number in inputs:
  if number == 0:
    if current_case:
      cases.append(current_case)
      current_case=[]
  else:
    current_case.append(number)

for i, case in enumerate(cases, 1):
  print(card_game_simulation(case))
  print()