# i - 1 까지의 파란색의 수, 빨간색의 수, 최대합이 같으면 같은 상황이다!!
# dp[i][j] = i번째 칸을 반드시 선택했을 때, 파란색 카드의 수는 j이다.
# 빨간색 수는 고려할 필요없음. 파란색 카드가 n개면 자연스럽게 빨간색 카드고 n개가 된다!
# i번째 파란색 선택 dp[i][j] = dp[i-1][j-1] + board[i][1]
# i번째 파란색 미선택 dp[i][j] = dp[i-1][j] + board[i][0]
n = int(input())
# 빨간색, 파란색
board = [0] + [list(map(int, input().split())) for _ in range(2 * n)]
inf = int(1e9)
dp = [[-inf for _ in range(n + 1)] for _ in range(2 * n + 1)]

dp[0][0] = 0

for i in range(1, 2 * n + 1):
    red_card, blue_card = board[i]
    for j in range(n + 1):
        if i - 1 >= 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j] + red_card)
            if j - 1 >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + blue_card)

# 파란색 카드 절반, 빨간색 카드 절반
print(dp[2 * n][n])