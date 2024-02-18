n = int(input())
nums = list(map(int, input().split()))

from heapq import heappush, heappop
max_heap = []
for x in nums:
    heappush(max_heap, -x)

while len(max_heap) >= 2:
    q1 = -heappop(max_heap)
    q2 = -heappop(max_heap)
    if q1 != q2:
        heappush(max_heap, -abs(q1 - q2))


if len(max_heap) == 0:
    print(-1)
else:
    print(*max_heap)