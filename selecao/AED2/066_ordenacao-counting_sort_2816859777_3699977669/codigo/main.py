def get_index_list(list):
  index_list = []
  for i in list:
    index_list.append(int(i[1]*10))
  return index_list

def get_min_max(list):
  min = list[0]
  max = min
  for i in list:
    if i < min:
      min = i
    if i > max:
      max = i
  return (min, max)

def make_list(length):
  list = []
  for i in range(0, length):
    list.append([])
  return list

def pigeonhole_sort(list):
  index_list = get_index_list(list)
  min, max = get_min_max(index_list)
  m = make_list(max - min + 1)

  for i in list:
    m[int(i[1]*10 - min)].append(i)

  key = 0
  for alunos in reversed(m):
    for v in alunos:
      list[key] = v
      key += 1
    
    
list = eval(input())

pigeonhole_sort(list)

length = len(list)
position = 0
for i in list:
  position += 1
  print(position, ". ", i[0], " - ", i[1] * 1.0, sep="")