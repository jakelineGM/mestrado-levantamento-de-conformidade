from ast import literal_eval
import sys

def max_heapify(A, i=0):
  n = len(A)
  largest = i
  left = 2 * i + 1
  right = 2 * i + 2

  if left < n and A[left] > A[largest]:
      largest = left
  if right < n and A[right] > A[largest]:
      largest = right

  if largest != i:
      A[i], A[largest] = A[largest], A[i]
      max_heapify(A, largest)

def main():
    for line in sys.stdin:
        arr = literal_eval(line.strip())
        if arr ==[]:
           break
        max_heapify(arr, 0)
        print(arr)
if __name__ == "__main__":
    main()

    
    