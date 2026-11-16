from collections import deque

def terminal_simulation(q, tasks):
  
  queue = deque(tasks)
  total_time = 0

  while queue:
    current_task = queue.popleft()

    if current_task <= q:
      total_time += q
      # current_time += q
    else:
      total_time += q
      # current_time += q
      remaining_time = current_task - q
      if remaining_time > 0:
        queue.append(remaining_time)

  total_time -= (q - current_task) if current_task <= q else 0

  return total_time

while True:
  entrada_q = input().strip()

  if not entrada_q:
    break

  if not entrada_q.isdigit():
    break
    
  q = int(entrada_q)

  if q == 0:
    break

  #entrada_tasks = input().strip()
  #if not entrada_tasks:
  #    break
  
  #tasks = list(map(int, entrada_tasks.split()))
  tasks = []
  for x in input().split():
    tasks.append(int(x))
  
  print(terminal_simulation(q, tasks))
  break
  