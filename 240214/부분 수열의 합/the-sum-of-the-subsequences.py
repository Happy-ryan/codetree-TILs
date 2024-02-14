n, m = map(int, input().split())
nums = list(map(int, input().split()))
dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
inf = int(1e9)
# 풀이1
# 특정한 값을 만드는 dp유형, 순서 고정, 1개만 사용!! > 거꾸로 봐야해!!
# dpf(i, j) = i번째 숫자를 썼을 때 합이 J이다.
def dpf(i, j):
    if i == 0:
        if j == 0:
            return 0
        else:
            return inf
    if j < 0:
        return inf

    if dp[i][j] != -1:
        return dp[i][j]

    ret = min(dpf(i - 1, j), dpf(i - 1, j - nums[i]) + 1)

    dp[i][j] = ret

    return ret

ans = dpf(n - 1, m)
if ans >= inf:
    ans = 'No'
else:
    ans = 'Yes'

print(ans)

#