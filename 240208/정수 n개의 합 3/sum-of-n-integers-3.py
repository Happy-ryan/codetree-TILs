n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def make_psum(board):
    n = len(board)
    psum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n):
        for j in range(n):
            psum[i + 1][j + 1] = board[i][j] + psum[i + 1][j] + psum[i][j + 1] - psum[i][j]

    return psum

def range_sum(r1, c1, r2, c2):
    return psum[r2 + 1][c2 + 1] - psum[r2 + 1][c1] - psum[r1][c2 + 1] + psum[r1][c1]

psum = make_psum(board)

max_val = 0
for r1 in range(n - k + 1):
    for c1 in range(n - k + 1):
        r2 = r1 + k - 1
        c2 = c1 + k - 1
        max_val = max(max_val, range_sum(r1, c1, r2, c2))

print(max_val)