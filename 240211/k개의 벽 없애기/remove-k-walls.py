# bfs: O(N^2) = 100^2
# 벽 선택: O(8Ck) = 8C4
# 시작점과 도착점은 1개!
# BFS + 브루트포스!!(제거할 벽 선택!)
from collections import deque
from itertools import combinations

inf = int(1e9)

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

r1 -= 1
c1 -= 1
r2 -= 1
c2 -= 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(r1, c1, r2, c2, board):
    dq = deque([])

    visited = [[inf for _ in range(n)] for _ in range(n)]
    in_queue = [[False for _ in range(n)] for _ in range(n)]

    dq.append((r1, c1))
    in_queue[r1][c1] = True
    visited[r1][c1] = 0

    while dq:
        cr, cc = dq.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc) and not in_queue[nr][nc]  and board[nr][nc] == 0:
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                visited[nr][nc] = visited[cr][cc] + 1

    if visited[r2][c2] >= inf:
        return inf
    else:
        return visited[r2][c2]


def find_wall():
    walls = []
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                walls.append((i, j))
    return walls


walls = find_wall()
min_val = inf
for rows in combinations(walls, k):
    for row in rows:
        board[row[0]][row[1]] = 0
    min_val = min(min_val, bfs(r1, c1, r2, c2, board))
    for row in rows:
        board[row[0]][row[1]] = 1

if min_val == inf:
    min_val = -1

print(min_val)