n = int(input())

import sys
sys.setrecursionlimit(n**2)


board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

inf = int(1e8)

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# dpf(r, c): 임의의 출발점에 대해서 도착점(r, c)까지 올 수 있는 최대거리
# dpf(r, c) = max(dpf(br, bc) where br, bc is adj && board[br][bc] < board[r][c]) + 1 <- 항상 식부터!!

def dpf(r, c):
    # dp 있다! 종료!
    if dp[r][c] != -1:
        return dp[r][c]

    # 점화식
    is_start = True
    ret = -inf
    for k in range(4):
        br, bc = r + dr[k], c + dc[k]
        if in_range(br, bc) and board[r][c] > board[br][bc]:
            is_start = False
            ret = max(ret, dpf(br, bc) + 1)  


    # 시작점 - 출발점일 때...
    if is_start:
        return 1

    dp[r][c] = ret

    return ret

max_ret = 0
for r in range(n):
    for c in range(n):
        max_ret = max(max_ret, dpf(r, c))

print(max_ret)