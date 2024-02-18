from heapq import heappush, heappop
n = int(input())
nums = list(map(int, input().split()))
# 평균이 최대가 되려면 작은 값을 최대한 날려야함!!
def cal(k, nums):
    min_heap = []
    for num in nums:
        heappush(min_heap, num)
    for _ in range(k):
        heappop(min_heap)
    
    return sum(min_heap) / len(min_heap)

ans = 0
for k in range(1, n - 1):
    ans = max(ans, cal(k, nums))

print(f"{ans:0.2f}")