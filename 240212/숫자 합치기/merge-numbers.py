from heapq import heappush, heappn = int(input())
nums = list(map(int, input().split()))

heap = []
cost = 0

for x in nums:
    heappush(heap, x)

# 최솟값 뽑을 때마다 min 쓰면 시간초과
while len(heap) >= 2:
    q1 = heappop(heap)
    q2 = heappop(heap)

    cost += q1 + q2

    heappush(heap, q1 + q2)


print(cost)