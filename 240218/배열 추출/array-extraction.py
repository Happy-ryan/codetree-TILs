from heapq import heappush, heappop

n = int(input())
max_heap = []

for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(max_heap, -x)
    else:
        if len(max_heap) == 0:
            print(0)
        else:
            print(-heappop(max_heap))