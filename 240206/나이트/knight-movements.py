n = int(input())
r1, c1, r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

in_queue = [[False for _ in range(n)] for _ in range(n)]
inf = int(1e8)
visited = [[inf for _ in range(n)] for _ in range(n)]


from collections import deque

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n and not in_queue[r][c]

def bfs(starts):

    dr = [-2, -1, 1, 2, -2, -1, 1, 2]
    dc = [-1, -2, -2, -1, 1, 2, 2, 1]

    dq = deque([])

    for r, c in starts:
        dq.append((r, c))
        visited[r][c] = 0

    while dq:
        cr, cc = dq.popleft()
        for dir in range(8):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc):
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                visited[nr][nc] = visited[cr][cc] + 1

starts = [(r1, c1)]
bfs(starts)
ans = visited[r2][c2]
if ans >= inf:
    ans = -1

print(ans)