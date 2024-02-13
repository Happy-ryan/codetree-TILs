# 정렬은 불가
# 쌍 문제는 하나을 고정한다!!
n = int(input())
nums = list(map(int, input().split()))
# 누적 최소값
inf = int(1e9)
pmin = [inf for _ in range(n + 1)]

ans = inf
for i in range(n):
    pmin[i + 1] = min(pmin[i], nums[i])

ans = 0
for i in range(n):
    if nums[i] == pmin[i + 1]:
        continue
    ans = max(ans, nums[i] -pmin[i + 1])

print(ans)