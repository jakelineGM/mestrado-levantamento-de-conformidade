def max_heapify(array, n, index):
  left_child_index = 2 * index + 1
  right_child_index = 2 * index + 2


  if left_child_index < n and array[left_child_index] > array[index]:
    largest_element_index = left_child_index

  else:
    largest_element_index = index
 
  if right_child_index < n and array[right_child_index] > array[largest_element_index]:
    largest_element_index = right_child_index

  if largest_element_index != index:
    array[index], array[largest_element_index] = array[largest_element_index], array[index]
    max_heapify(array, n, largest_element_index)

heaps = [[]]

while True:
  heap = eval(input())
  
  if not heap:
    break
  
  heaps.append(heap)
  del heaps[0]

  for i in heaps:
    max_heapify(i, len(i), 0)
    print(i)
