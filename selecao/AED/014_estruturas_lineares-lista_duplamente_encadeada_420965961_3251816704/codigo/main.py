def create_node(val):
  new = dict()
  new['val'] = val
  new['suc'] = None
  new['ant'] = None
  return new


def create_stack():
  stack = dict()

  stack['top'] = None
  stack['low'] = None
  stack['size'] = 0
  
  return stack

def stack_size(stack):
  return stack['size']

def push(stack,val):
  node = create_node(val)
  if(peek(stack) == None):
    stack['top'] = node
    stack['low'] = node
    node['suc'] = node
    node['ant'] = node
  else:
    node['suc'] = stack['top']
    node['ant'] = stack['top']['ant']
    stack['top']['ant'] = node
    stack['low']['suc'] = node
    stack['top'] = node

  #print(f"pushed {stack['top']}")
  stack['size'] += 1

def pop(stack):
  val = stack['top']['val']
  if(stack_size(stack) == 1):
    stack['top']['ant'] = None
    stack['top']['suc'] = None
    stack['top'] = None
    stack['low'] = None

  else:
    stack['top']['suc']['ant'] = stack['top']['ant']
    stack['top']['ant']['suc'] = stack['top']['suc']
    stack['top'] = stack['top']['suc']

  stack['size'] -=1
  return val
  
def append(stack,val):
  node = create_node(val)
  if(peek(stack) == None):
    stack['top'] = node
    node['suc'] = node
    node['ant'] = node
  else:
    stack['low']['suc'] = node
    node['ant']  = stack['low']
    node['suc'] = stack['top']
    stack['top']['ant'] = node
    stack['low'] = node
  stack['size'] += 1  

  
def stack_cards(lis):
  stack = create_stack()

def print_stack(stack):
  walker = stack['top']
  while(walker != stack['low']):
    print(f"{walker['val'] }",end=" ")
    walker = walker['suc']
  print()

def peek(stack):
  return stack['top']

  
values = [int(i) for i in input().split(" ")]
index = 0
val = values[index]
#print(f"loops {len(values) -1}")
while(val != 0):
  list = [i for i in range(1,val + 1)]
  list = list[::-1]
  stack = create_stack()
  for num in list:
    push(stack,num)
  #  print_stack(stack)
  discarded = []
  while(stack['top'] != stack['low'] and stack_size(stack) != 1):
    discarded.append(pop(stack))
    last = pop(stack)
    append(stack,last)
  print("Descartadas: ", end = "")
  for val in discarded:
    print(f"{val}",end=" ")
  print(f"\nRestou: {peek(stack)['val']}")
  index +=1
  val = values[index]
  if(val == 0):
    break;
  print()
  