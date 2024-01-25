# dp[r][c]: (0, n-1) 에서 출발해서 (r, c)에 도착하기까지 경로위의 수의 합 중 최소값.
# dpf(r, c) = min(dpf(r-1, c), dpf(r, c+1)) + val[r][c]
# 1. no recursive
# 2. DAG: directed acycle graph
#   - indegree = 0: 나를 구하는 데에 다른게 필요 없음.

n = int(input())

board = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]
INF = int(1e8)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def dpf(r, c):

    if dp[r][c] != -1:
        return dp[r][c]
    # in_degree 가 0인 지점
    if not in_range(r-1, c) and not in_range(r, c+1):
        return board[r][c]

    ret = INF
    if in_range(r-1, c): # up
        ret = min(ret, dpf(r-1, c) + board[r][c])
    if in_range(r, c+1): # right
        ret = min(ret, dpf(r, c+1) + board[r][c])
    #memo
    dp[r][c] = ret
    return ret

print(dpf(n - 1, 0))