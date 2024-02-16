# 같은 상황: i번째를 선택했을 때, 그 전까지의 (+의 개수, -의 개수, 합)이 동일하면 같은 상황
# dp[i][j]: i번째 숫자를 선택했을 때, 숫자j를 만들 수 있는 경우의 수!
# dp[i][j] = dp[i - 1][j + num], dp[i - 1][j - num] where -20 <= j +- num <= 20
# m을 -20으로 하면 인덱스 처리가 어려움, m += 20 .. 0 <= m <= 40
n, m = map(int, input().split())
base = 20
nums = [0] + list(map(int, input().split()))
inf = int(1e9)
max_range = base * 2 + 1
dp = [[0 for _ in range(max_range)] for _ in range(n + 1)]

dp[0][0 + base] = 1
for i in range(1, n + 1):
    for j in range(max_range):
        if 0 <= j + nums[i] < max_range:
            dp[i][j] += dp[i - 1][j + nums[i]] 
        if 0 <= j - nums[i] < max_range:
            dp[i][j] += dp[i - 1][j - nums[i]] 

print(dp[n][m + base])