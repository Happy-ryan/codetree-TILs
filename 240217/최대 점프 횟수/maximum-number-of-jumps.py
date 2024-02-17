import sys
sys.setrecursionlimit(10**5)

n = int(input())
nums = list(map(int, input().split()))
inf = int(1e9)

def sol_1():
    dp = [-1 for _ in range(n)]
    # dpf(x) x번에 도달했을 때 최대점프횟수
    # dpf(x) = max(retm, dpf(i) + 1) where x - i = nums[i] 
    def dpf(x):
        if dp[x] != -1:
            return dp[x]

        ret = -inf
        for i in range(x):
            if x - i <= nums[i]:
                ret = max(ret, dpf(i) + 1)

        if x == 0:
            return 0

        dp[x] = ret

        return ret

    ans = -inf
    for i in range(n):
        ans = max(ans, dpf(i))

    return ans


print(sol_1())