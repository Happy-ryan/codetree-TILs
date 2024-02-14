# 중복을 사용할 수 있는 dp
n = int(input())
# n원을 나타낼 수 있는 경우의 수

# dpf(i) = dpf(i-1) + dfs(i-2) + dpf(i-5)

#풀이1
def solution_1(n):
    dp = [-1 for _ in range(n + 1)]
    # dp[n] = dp[n - 1] + dp[n - 2] + dp[n - 5]
    # 특정값을 만드는 방법의 수 + 순서가 다르면 다른 조합!
    mod = 10007
    # 5 - 5 = 0 1개 필요..dp[0] = 1
    dp[0] = 1

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = (dp[i - 1]) % mod
        elif i < 5:
            dp[i] = (dp[i - 1] + dp[i - 2]) % mod
        else:
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 5]) % mod

    return dp[n]

# 풀이2
def solution_2(n):
    dp = [-1 for _ in range(n + 1)]

    # n을 만들기 위한 경우의 수 + 순서가 다르면 다른 조합
    def dpf(x):
        if x == 0:
            return 1
        if dp[x] != -1:
            return dp[x]
        
        ret = 0
        if x == 1:
            ret += 1
        elif x < 5:
            ret += dpf(x - 1) + dpf(x - 2)
        else:
            ret += dpf(x - 1) + dpf(x - 2) + dpf(x - 5)

        dp[x] = ret

        return ret

    return dpf(n)
        
print(solution_2(n))