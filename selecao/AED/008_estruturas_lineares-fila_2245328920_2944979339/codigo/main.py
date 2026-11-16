from collections import deque

def terminal_simulation(Q: int, times: list[int]) -> int:
    queue = deque(times)
    total_time = 0

    while queue:
        current = queue.popleft()
        if current <= Q:
            if not queue: # last student
                total_time += current
            else:
                total_time += Q
        else:
            total_time += Q
            queue.append(current - Q)

    return total_time

def main():
    Q = int(input().strip())
    times = list(map(int, input().split()))
    result = terminal_simulation(Q, times)
    print(result)

if __name__ == "__main__":
    main()



  