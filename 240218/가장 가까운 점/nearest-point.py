from heapq import heappush, heappop

n, m = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(n)]

min_heap = []
for i in range(n):
    x, y = points[i]
    d = abs(x) + abs(y)
    heappush(min_heap, (d, x, y))

for _ in range(m):
    d, x, y = heappop(min_heap)
    x += 2
    y += 2
    d = abs(x) + abs(y)
    heappush(min_heap, (d,x, y))

print(min_heap[0][1], min_heap[0][2])