n, m = map(int, input().split())
coins = list(map(int, input().split()))
coins.sort()
# 특정한 숫자를 만드는 유형, 순서 무관, 최대 동전의 수를 찾는 유형
def solution_1(m):
    # dp의 정의: m원을 만들기 위한 최대 동전의 수
    inf = int(1e9)
    dp = [-inf for _ in range(m + 1)]
    # 특정수를 만들 때 '0'은 반드시 1가지 경우로 생각을 해야한다. -> 경우의 수
    # 동전의 수 유형에서는 dp[0] = 0
    dp[0] = 0
    # dp[i] = max(dp[i - coin] + 1) where i >= coin
    for money in range(1, m + 1):
        for coin in coins:
            if coin <= money:
                dp[money] = max(dp[money - coin] + 1, dp[money])
    ans = dp[m]
    if ans >= -inf:
        ans = -1
    return ans

print(solution_1(m))