n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

from collections import deque

def in_range(r, c):
    return 0 <= r < n and 0 <= c < m

def bfs(r, c):
    
    q = deque([])

    q.append((r, c))
    visited[r][c] = True

    cnt = 0
    while q:
        cr, cc = q.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 1:
                q.append((nr, nc))
                cnt += 1
                visited[nr][nc] = True

bfs(0, 0)

if visited[n - 1][m - 1]: 
    print(1)
else:
    print(0)