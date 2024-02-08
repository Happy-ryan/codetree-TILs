n, m, k = map(int, input().split())
board = [list(input()) for _ in range(n)]

def make_psum_alpabet(target: str, board):
    n, m = len(board), len(board[0])

    converted_board = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if board[i][j] == target:
                converted_board[i][j] = 1

    psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            psum[i + 1][j + 1] = converted_board[i][j] + psum[i + 1][j] + psum[i][j + 1] - psum[i][j]

    return psum

def range_sum(psum, r1, c1, r2, c2):
    return psum[r2 + 1][c2 + 1] - psum[r2 + 1][c1] - psum[r1][c2 + 1] + psum[r1][c1]

psum_a = make_psum_alpabet('a', board)
psum_b = make_psum_alpabet('b', board)
psum_c = make_psum_alpabet('c', board)

for _ in range(k):
    r1, c1, r2, c2 = map(int, input().split())
    r1 -= 1
    c1 -= 1
    r2 -= 1
    c2 -= 1
    print(range_sum(psum_a, r1, c1, r2, c2), range_sum(psum_b, r1, c1, r2, c2), range_sum(psum_c, r1, c1, r2, c2))