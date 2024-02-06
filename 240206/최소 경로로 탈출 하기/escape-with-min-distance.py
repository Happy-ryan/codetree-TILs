# 가중치가 동일한 그래프에서의 bfs
# bfs 유형에서 시작점이 단일인지 복수인지 판단하는게 매우 중요함
# bfs 이동가능한 영역의 넓이 구하는 방법

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
in_queue = [[False for _ in range(m)] for _ in range(n)]
inf = int(1e9)
visited = [[inf for _ in range(m)] for _ in range(n)]

from collections import deque

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m and not in_queue[r][c]

def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    dq = deque([])

    dq.append((0, 0))
    visited[0][0] = 0

    while dq:
        cr, cc = dq.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc) and board[nr][nc] == 1:
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                visited[nr][nc] = visited[cr][cc] + 1 

bfs()



ans = visited[n - 1][m - 1]
if ans >= inf:
    ans = -1
print(ans)