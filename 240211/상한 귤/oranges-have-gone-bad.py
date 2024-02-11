# 백준 - 토마토 문제와 비슷한거같음..

from collections import deque
inf = int(1e9)

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 상한 귤 찾기!
def find(board):
    starts = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 2:
                starts.append((r, c))
    return starts

# 상한 귤들을 먼저 처리
# 핵심! 귤이 상하면 1 -> 2로 변경된다!!
def bfs(starts):
    dq = deque([])
    in_queue = [[False for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    for r, c in starts:
        dq.append((r, c))
        in_queue[r][c] = True

    while dq:
        cr, cc = dq.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == 1:
                dq.append((nr, nc))
                board[nr][nc] = 2 # 귤이 상함 1 > 2
                in_queue[nr][nc] = True
                visited[nr][nc] = visited[cr][cc] + 1

    
    for r in range(n):
        for c in range(n):
            # 귤이 없었네요~
            if board[r][c] == 0:
                visited[r][c] = -1
            # 귤이 있는데(1) & 방문하지 않음(상하지않음)
            elif board[r][c] == 1 and visited[r][c] == 0:
                visited[r][c] = -2


    for row in visited:
        print(*row)

starts = find(board)
bfs(starts)