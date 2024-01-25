n = int(input())
board = [list(map(int, input().split())) for _  in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

inf = int(1e8)

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n
# dpf(r, c): (0, 0) ~ (r, c)에 도착하기까지 경로위의 수 중에서 최솟값
def dpf(r, c):

    if dp[r][c] != -1:
        return dp[r][c]

    if not in_range(r - 1, c) and not in_range(r, c - 1):
        return board[r][c]

    ret = -inf
    if in_range(r, c - 1):
        # ret을 최대로 갱신하고 싶음: 최솟값 중 최대값....
        ret = max(ret, min(dpf(r, c - 1), board[r][c]))
    
    if in_range(r - 1, c):
        ret = max(ret, min(dpf(r - 1, c), board[r][c]))

    dp[r][c] = ret

    return ret      


print(dpf(n - 1, n - 1))