n = int(input())
nums = [0] + list(map(int, input().split()))

def sol_1():
    max_m = sum(nums)
    inf = int(1e9)
    dp = [[inf for _ in range(max_m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        for j in range(max_m, -1, -1):
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - nums[i]] + 1)

    # for row in dp:
    #     print(*row)

    if max_m % 2 != 0:
        return 'No'
    else:
        target = max_m // 2
        if dp[n][target] >= inf:
            return 'No'
        else: 
            return 'Yes'

print(sol_1())