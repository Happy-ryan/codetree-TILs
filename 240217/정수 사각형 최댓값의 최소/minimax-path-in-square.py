inf = int(1e9)

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

dr = [1, 0]
dc = [0, 1]

# 최댓값의 최소값
# dpf(r, c) = min(ret, max(dpf(r - 1, c), board[r][c]))
# dpf(r, c) = min(ret, max(dpf(r, c - 1), board[r][c]))

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def dpf(r, c):
    if dp[r][c] != -1:
        return dp[r][c]

    if r == 0 and c == 0:
        return board[r][c]
    
    ret = inf
    if in_range(r - 1, c):
        ret = min(ret, max(dpf(r - 1, c), board[r][c]))
    
    if in_range(r, c - 1):
        ret = min(ret, max(dpf(r, c - 1), board[r][c]))

    dp[r][c] = ret

    return ret

print(dpf(n - 1, n - 1))