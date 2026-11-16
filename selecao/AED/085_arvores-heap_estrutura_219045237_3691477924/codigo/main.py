def max_heapify(arr,n,i):
  largest = i
  l = 2 * i + 1
  r = 2*i+2
  if l<n and arr[i] < arr[l]:
    largest = l

  if r<n and arr[largest] < arr[r]:
    largest = r

  if largest != i:
    arr[i], arr[largest] = arr[largest], arr[i]
    max_heapify(arr,n,largest)
def main():
  output = ""
  while True:
    input_list =input()

    try: 
        arr = eval(input_list)
        if arr == []:
            break
        if not all(isinstance(x, int) for x in arr):
            raise ValueError("insira apenas inteiros")
        n = len(arr)
        max_heapify(arr,n,0)
        output += str(arr) + "\n"
    except:
      print("entrada invalida")
  print(output.rstrip())
if __name__ == "__main__":
    main()