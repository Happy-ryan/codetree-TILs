from heapq import heappush, heappop, heapify

n, m = map(int, input().split())
nums = list(map(int, input().split()))

max_heap = []
for i in range(n):
    heappush(max_heap, -nums[i])

for _ in range(m):
    max_q = -heappop(max_heap)
    max_q -= 1
    heappush(max_heap, -max_q)

print(-heappop(max_heap))