# 두 집합의 차이가 적은 것을 찾아야함
# 8 7 6 2
# (최대, 최소)로 구성

from heapq import heappush, heappop
max_heap = []
min_heap = []

t = int(input())
m = 0
for _ in range(t):
    x, y = map(int, input().split())
    m += x
    for _ in range(x):
        heappush(max_heap, -y)
        heappush(min_heap, y)

ans = 0
for _ in range(m // 2):
    max_q = -heappop(max_heap)
    min_q = heappop(min_heap)
    # print(f"max: {max_q}, min: {min_q}")
    ans = max(ans, max_q + min_q)

print(ans)