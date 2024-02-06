from collections import deque

n, h, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
inf = int(1e8)

def find_grid():
    people = []
    safe = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 3:
                safe.append((r, c))
    return safe



def bfs(r, c, safe):
    dq = deque([])

    in_queue = [[False for _ in range(n)]  for _ in range(n)]
    visited = [[inf for _ in range(n)] for _ in range(n)]


    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n and not in_queue[r][c] and board[r][c] != 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dq.append((r, c))
    visited[r][c] = 0

    while dq:
        cr, cc = dq.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc):
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                visited[nr][nc] = visited[cr][cc] + 1

    min_time = inf
    for r, c in safe:
        min_time = min(min_time, visited[r][c])
    
    return min_time


safe = find_grid()
# 기존에 틀렸던 이유 - 각 좌표마다 새롭게 bfs를 진행하는데 visited랑 in_queue가 초기화 되지 않고 전역변수로 사용되었음,
final = [[0 for _ in range(n)] for _ in range(n)]
for r in range(n):
    for c in range(n):
        if board[r][c] == 2:
            time = bfs(r, c, safe)
            if time >= inf:
                time = -1
            final[r][c] = time

for row in final:
    print(*row)