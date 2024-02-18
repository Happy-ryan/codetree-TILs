n = int(input())
nums = list(map(int, input().split()))

from heapq import heappush, heappop
max_heap = []
for x in nums:
    heappush(max_heap, -x)

while len(max_heap) >= 2:
    q1 = -heappop(max_heap)
    q2 = -heappop(max_heap)
    heappush(max_heap, abs(q1 - q2))


print(*max_heap)