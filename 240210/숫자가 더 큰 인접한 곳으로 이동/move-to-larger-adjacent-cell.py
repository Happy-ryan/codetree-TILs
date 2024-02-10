n, r, c = map(int, input().split())
r -= 1
c -= 1
board = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

ans = [board[r][c]]
while True:
    cur_val = board[r][c]
    can_move = False
    for dir in range(4):
        nr, nc = r + dr[dir], c + dc[dir]
        if in_range(nr, nc) and cur_val < board[nr][nc]:
            can_move = True
            # 다음 좌표로 위치 옮김
            ans.append(board[nr][nc])
            r, c = nr, nc
            break
    if not can_move:
        break

print(*ans)