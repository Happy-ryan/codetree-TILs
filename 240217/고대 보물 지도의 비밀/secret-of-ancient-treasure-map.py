n, k = map(int, input().split())
nums = [0] + list(map(int, input().split()))

# 2차원dp 음수의 개수를 기록
# dp[i][j]: i번째 숫자를 반드시 선택했을 때 음수의 개수는 j이다. 값은 i번째 숫자를 선택햇을 때까지의 합
# 현재 인덱스까지의 합과 음수의 수가 일치하면 같은 상황!!
# 연속하게 가지고 오려면 반드시 dp[i - 1]에만 가져와야함...
# dp[i - 2] 연속불가!!

inf = int(1e9)
dp = [[-inf for _ in range(k + 1)] for _ in range(n + 1)]

dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(k + 1):
        if nums[i] >= 0:
            # 연속을 끊고 내 자신을 선택할 수 있어야함!
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + nums[i], nums[i])
        else:
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + nums[i], nums[i])
            

ans = 0
for row in dp:
    ans = max(ans, max(row))

print(ans)