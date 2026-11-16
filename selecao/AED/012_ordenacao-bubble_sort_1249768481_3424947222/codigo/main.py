from typing import List, TypeVar


T = TypeVar('T')


def bubble_sort(array: List[T]):
  '''
  Change array so it become sorted
  '''
  size = len(array)

  for i in range(size):
    swapped_elements = False
    for j in range(size - i - 1):
      if array[j] > array[j+1]:
        # Swap elements
        swapped_elements = True
        print(f"{array[j]} <-> {array[j+1]}")
        array[j], array[j+1] = array[j+1], array[j]
    if not swapped_elements:
      return
        

if __name__ == "__main__":
  try:
    input_array = eval(input())
    bubble_sort(input_array)
    print(input_array)
  except Exception as e:
    print(f"Failed to sort: {e}")
