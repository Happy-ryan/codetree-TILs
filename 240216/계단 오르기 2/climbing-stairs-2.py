n = int(input())
coins = [0] + list(map(int, input().split()))


# dp[i] i층을 반드시 선택했을 때 얻을 수 있는 최대 동전의 수
# 1칸 오르는 것은 기록해둬야함!! 최대 3번이므로
# dp[i][j] i층을 도달, 1칸을 점핑을 사용한 횟수
# if) 1칸 점핑 dp[i - 1]
# if) 2칸 점핑 dp[i - 2]

inf = int(1e9)
dp = [[-inf for _ in range(4)] for _ in range(n + 1)]


dp[0][0] = 0
# dp[i][j] = max(dp[i - 1][j - 1], dp[i - 2][j]) + coins[i]
for i in range(1, n + 1):
    for j in range(4):
        if i == 1:
            dp[1][1] = coins[i]
        else:
            if j == 0:
                dp[i][j] = dp[i - 2][j] + coins[i]
            else:
                dp[i][j] = max(dp[i - 1][j - 1], dp[i - 2][j]) + coins[i]

print(max(dp[n]))