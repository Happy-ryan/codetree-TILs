n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dfs(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    # 도착지점에 도착 > 갱신
    if r == n - 1 and c == 0:
        return board[r][c]

    dr = [1, 0]
    dc = [0, -1]

    min_sum = 1000000 * 100
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]

        if in_range(nr, nc):
            min_sum = min(min_sum, dfs(nr, nc) + board[r][c])
            
    dp[r][c] = min_sum

    return min_sum


print(dfs(0, n - 1))