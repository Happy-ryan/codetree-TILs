def find_one(board):
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                res.append((i, j))
    return res


def is_range(r, c):
    return 0 <= r < n and 0 <= c < n and board[r][c] == 0


def bomb_1(board, r, c):
    dirs = [(- 1, 0), (- 2, 0), (1, 0), (2, 0)]
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if is_range(nr, nc):
            board[nr][nc] = 1


def bomb_2(board, r, c):
    dirs = [(- 1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if is_range(nr, nc):
            board[nr][nc] = 1


def bomb_3(board, r, c):
    dirs = [(- 1, -1), (-1, 1), (1, -1), (1, 1)]
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if is_range(nr, nc):
            board[nr][nc] = 1


def bomb_board(board, bomb_number: list[int]):
    for (r, c), bomb in zip(bomb_list, bomb_number):
        if bomb == 1:
            bomb_1(board, r, c)
        elif bomb == 2:
            bomb_2(board, r, c)
        elif bomb == 3:
            bomb_3(board, r, c)
    
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                cnt += 1

    return cnt

from copy import deepcopy

max_region = 0
def dfs(level, k):
    global max_region
    if level == k:
        new_board = deepcopy(board)
        max_region = max(max_region, bomb_board(new_board, ans.copy()))
        return

    for i in range(1, 4):
        ans.append(i)
        dfs(level + 1, k)
        ans.pop()


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
bomb_list = find_one(board)
k = len(bomb_list)
ans = []
dfs(0, k)
print(max_region)