n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dir_board = [list(map(int, input().split())) for _ in range(n)]


dir_list = [(), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
cr, cc = map(int, input().split())
cr -= 1
cc -= 1


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n


def can_move(cr, cc, nr, nc):
    return board[nr][nc] > board[cr][cc]

ans = 0
step = []
def dfs(cr, cc):
    global ans
    ans = max(ans, len(step))
    
    cur_dir = dir_list[dir_board[cr][cc]]
    for val in range(1, n + 1):
        nr = cr + cur_dir[0] * val
        nc = cc + cur_dir[1] * val
        if in_range(nr, nc) and can_move(cr, cc, nr, nc):
            step.append(board[nr][nc])
            dfs(nr, nc)
            step.pop()

dfs(cr, cc)
print(ans)