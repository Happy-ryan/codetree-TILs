from heapq import heappush, heappop
n = int(input())
max_heap = []

for _ in range(n):
    cmd = list(input().split())
    if cmd[0] == 'push':
        heappush(max_heap, -int(cmd[1]))
    elif cmd[0] == 'size':
        print(len(max_heap))
    elif cmd[0] == 'empty':
        if len(max_heap) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'pop':
        max_q = -heappop(max_heap)
        print(max_q)
    elif cmd[0] == 'top':
        print(max_heap[0])