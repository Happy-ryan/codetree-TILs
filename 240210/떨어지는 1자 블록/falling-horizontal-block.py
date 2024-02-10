n, m, k = map(int, input().split())
# 블록의 시작점(가장 왼쪽)
k -= 1
board = [list(map(int, input().split())) for _ in range(n)]

row = 0
while True:
    can_move = True
    # row가 지속적으로 초기화됨. while문 밖으로 이동
    if row >= n:
        can_move = False
    else:
        for col in range(k, m + k):
            if board[row][col] == 1:
                can_move = False
                break

    if not can_move:
        for col in range(k, m + k):
            board[row - 1][col] = 1
        break

    row += 1

for rowrow in board:
    print(*rowrow)