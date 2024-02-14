# 2차원 dp
n = int(input())
profit = [0] + list(map(int, input().split()))

# dp[i] = max(dp[i - x] + dp[x], profit(i))
# 중복 사용 가능
def solution_1():
    dp = [-1 for _ in range(n + 1)]
    dp[0] = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            dp[i] = max(dp[i - j] + profit[j], dp[i])

    
    return max(dp)

print(solution_1())