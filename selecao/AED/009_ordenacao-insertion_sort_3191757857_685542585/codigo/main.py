array = eval(input())
temp_array = array[0:]

print(array)

for i in range(1, len(array)):
  key = array[i]
  j = i - 1
  
  while j >= 0 and key < array[j]:
    array[j + 1] = array[j]

    if temp_array != array:
      temp_array = array[0:]
      print(temp_array)
    
    j = j - 1
  
  array[j + 1] = key
  
  if temp_array != array:
    temp_array = array[0:]
    print(temp_array)
