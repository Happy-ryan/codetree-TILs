from collections import defaultdict

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0, -1, 1, -1, 1]
dc = [0, 0, -1, 1, 1, 1, -1, -1]


def extract_number_pos(board, number):
    for r in range(n):
        for c in range(n):
            if board[r][c] == number:
                return r, c

def in_range(r, c):
    return 0 <= r < n and  0 <= c < n


def change_pos(r, c):
    max_pos, max_val = (0, 0), 0
    for k in range(8):
        nr, nc = r + dr[k], c + dc[k]
        if in_range(nr, nc) and board[nr][nc] > max_val:
            max_pos = (nr, nc)
            max_val = board[nr][nc]
    
    board[r][c], board[max_pos[0]][max_pos[1]] =  board[max_pos[0]][max_pos[1]], board[r][c]

    return board


for _ in range(m):
    for i in range(1, n * n + 1):
        r, c = extract_number_pos(board, i)
        board = change_pos(r, c)

for row in board:
    print(*row)