# 백준 - 토마토 문제와 비슷한거같음..
# t - 자신과 가장 가까운 상한 귤과의 거리를 의미함.
# 2 -> 1이 아니라 1 -> 2로 가는 상황을 보자!
from collections import deque
inf = int(1e9)

n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

def bfs(r, c):
    dq = deque([])
    in_queue = [[False for _ in range(n)] for _ in range(n)]
    visited = [[inf for _ in range(n)] for _ in range(n)]

    dq.append((r, c))
    in_queue[r][c] = True
    visited[r][c] = 0


    min_val = inf
    while dq:
        cr, cc = dq.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] != 0:
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                visited[nr][nc] = visited[cr][cc] + 1
            
                # 상한 귤까지의 최소 거리 찾기!
                if board[nr][nc] == 2:
                    min_val = min(min_val, visited[nr][nc])

    return min_val


for r in range(n):
    for c in range(n):
        if board[r][c] == 0:
            print(-1, end= " ")
        elif board[r][c] == 1:
            ans = bfs(r, c)
            if ans >= inf:
                ans = -2
            print(ans, end=" ")
        else:
            print(0, end= " ")
    print()