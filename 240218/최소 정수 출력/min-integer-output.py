from heapq import heappush, heappop

n = int(input())
min_heap = []
for _ in range(n):
    x = int(input())
    if x > 0:
        heappush(min_heap, x)
    else:
        if len(min_heap) == 0:
            print(0)
        else:
            print(heappop(min_heap))