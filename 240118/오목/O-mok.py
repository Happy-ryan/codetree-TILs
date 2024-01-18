# 시간복잡도
# O(N^2) : 바둑판 전부 돌아야함
# O(5 -> 1)
# O(N^2)
n = 19
board = [list(map(int, input().split())) for _ in range(19)]

# 
def in_range(r, c):
    return 0 <= r < 19  and 0 <= c < 19

# 특정 위치(양 끝점)의 바둑돌에 대해서 오목인지 파악하는 함수
# 0 2 2 2 2 2 0 0... 오목의 중간은 고려하지 않는다. 
# 무조건 양끝 점에서 오목이 되는지 확인한다.
# row 선행  ->->-> 그 다음 다음 줄..
# 따져야할 범위: (0, 1) / (1, 0) / (1, 1), (1, -1)
# 따라서 오목이라면 왼쪽끝(누워있는 경우), 맨위(일어서있는경우), || 왼쪽끝/오른쪽끝(대각선) 
dir = [(0, 1), (1, 0), (1, 1), (1, -1)]

def is_omok_horizontal(r, c):
    if board[r][c] == 0:
        return
    # 누워있는 경우
    # 오른쪽만 보면된다!
    cnt = 1
    for k in range(1, 5):
        nr, nc = r, c + k
        # print(f"nr: {nr}, nc: {nc}")
        if in_range(nr, nc) and board[r][c] == board[nr][nc]:
            cnt += 1
    if cnt == 5:
        return True
    return False

def is_omok_vertical(r, c):
    if board[r][c] == 0:
        return
    # 누워있는 경우
    # 밑에만 보면 된다!
    cnt = 1
    for k in range(1, 5):
        nr, nc = r + k, c
        # print(f"nr: {nr}, nc: {nc}, board: {board[nr][nc]}")
        if in_range(nr, nc) and board[r][c] == board[nr][nc]:
            cnt += 1
    if cnt == 5:
        return True
    return False

def is_omok_diagonal_right(r, c):
    if board[r][c] == 0:
        return
    # 대각선
    # 오른쪽끝 or 왼쪽끝일 수 있으므로 전부 확인해야함
    # 오른쪽 하방,왼쪽 하방을 점검할 필요가 있다.
    cnt_left = 1
    for k in range(1, 5):
        nr, nc = r + k, c + k
        # print(f"nr: {nr}, nc: {nc}, board: {board[nr][nc]}")
        if in_range(nr, nc) and board[r][c] == board[nr][nc]:
            cnt_left += 1


    if cnt_left == 5:
        return True
    return False


def is_omok_diagonal_left(r, c):
    if board[r][c] == 0:
        return
    # 대각선
    # 오른쪽끝 or 왼쪽끝일 수 있으므로 전부 확인해야함
    # 오른쪽 하방,왼쪽 하방을 점검할 필요가 있다.

    cnt_right = 1
    for k in range(1, 5):
        nr, nc = r + k, c - k
        # print(f"nr: {nr}, nc: {nc}, board: {board[nr][nc]}")
        if in_range(nr, nc) and board[r][c] == board[nr][nc]:
            cnt_right += 1

    if cnt_right == 5:
        return True
    return False

def solution():
    for r in range(19):
        for c in range(19):
            if is_omok_horizontal(r, c):
                # 정답은 1base + 1
                # 중간값 + 2
                # print("1", r, c)
                print(board[r][c])
                print(r + 1, c + 2 + 1)
                return
            if is_omok_vertical(r, c):
                # print("2", r, c)
                print(board[r][c])
                print(r + 2 + 1, c + 1)
                return
            if is_omok_diagonal_right(r, c):
                # print("3", r, c)
                print(board[r][c])
                print(r + 2 + 1, c + 2 + 1)
                return
            if is_omok_diagonal_left(r, c):
                # print("4", r, c)
                print(board[r][c])
                print(r + 2 + 1, c - 2 + 1)
                return
    print(0)
    return
solution()