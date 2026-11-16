import sys
def main(): 
  data = sys.stdin.read().split() 
  if not data: 
    return 

  q = int(data[0]) 
  queue = [int(x) for x in data[1:]] 

  total_time = 0 

  while queue: 
    current_job = queue.pop(0) 
  
    if current_job > q: 
      total_time += q 
      current_job -= q 
      queue.append(current_job) 
    else: 
      total_time += current_job 
      if queue: 
        total_time += (q - current_job) 

    print(total_time) 


main() 

