def find_bomb_position(board):
    res = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                res.append((i, j))
    return res


def is_range(r, c):
    return 0 <= r < n and 0 <= c < n


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
        max_region = max(max_region, bomb_board(new_board, ans))
        return

    for i in range(1, 4):
        ans.append(i)
        dfs(level + 1, k)
        ans.pop()


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
bomb_list = find_bomb_position(board)
k = len(bomb_list)
ans = []
dfs(0, k)
print(max_region)


# # 터진 영역 체크하고 추후 복구하기 위한 변수
# # 어떤 폭탄 타입이 폭탄인지에 따라서 복구영역이 달라지므로 타입에 대해서도 체크해놔야함.
# bombed = [[False for _ in range(n)] for _ in range(n)]
# bomb_type = [[0 for _ in range(n)] for _ in range(n)]
# # 폭탄 터질 자리
# bomb_pos = find_bomb_position(board)
# # 폭탄 터지기
# def bomb_bomb(r, c, b_type):
#     bomb_shapes = [
#         [],
#         [[-2, 0], [-1, 0], [0, 0], [1, 0], [2, 0]],
#         [[-1, 0], [1, 0], [0, 0], [0, -1], [0, 1]],
#         [[-1, -1], [-1, 1], [0, 0], [1, -1], [1, 1]]
#     ]
#     # 폭탄의 타입에 맞게 폭탄 터뜨리기
#     for i in range(5):
#         dr, dc = bomb_shapes[b_type][i]
#         nr, nc = r + dr, c + dc
#         if is_range(nr, nc):
#             bombed[nr][nc] = True