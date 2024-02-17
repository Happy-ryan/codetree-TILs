n = int(input())
nums = list(map(int, input().split()))

def sol_1():
    dp = [-1 for _ in range(n)]

    def dpf(x):
        if dp[x] != -1:
            return dp[x]
        
        ret = 0
        is_start = True
        for i in range(0, x):
            if nums[i] < nums[x]:
                ret = max(ret, dpf(i) + 1)
                is_start = False

        if is_start:
            return 1

        dp[x] = ret

        return ret

    ans = 0
    for i in range(n):
        ans = max(ans, dpf(i))

    return ans


print(sol_1())