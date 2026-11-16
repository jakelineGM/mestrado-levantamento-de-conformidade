def max_heapify(A, n, i):
    
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i

    
    if left < n and A[left] > A[largest]:
        largest = left

    
    if right < n and A[right] > A[largest]:
        largest = right

    
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        max_heapify(A, n, largest)


def main():
    while True:
        A = eval(input())  
        if A == []:  
            break
        n = len(A)
       
        max_heapify(A, n, 0)
        print(A)


if __name__ == "__main__":
    main()
