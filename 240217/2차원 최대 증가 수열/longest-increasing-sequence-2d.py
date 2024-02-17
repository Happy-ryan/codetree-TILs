n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(m)] for _ in range(n)]

inf = int(1e9)
def dpf(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    if r == 0 and c == 0:
        return 1

    ret = -inf
    for i in range(0, r):
        for j in range(0, c):
            if board[r][c] > board[i][j]:
                ret = max(ret, dpf(i, j) + 1)

    dp[r][c] = ret
    return ret

ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, dpf(i, j))

print(ans)