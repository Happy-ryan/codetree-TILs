# 출발점이 여러개인 bfs
# 이동 시 조건이 있는 bfs 높이차이는 u이상 d이하다!
# n 8이하 > 완탐 + bfs
from collections import deque
from itertools import combinations

n, k, u, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def choose_starts(k):
    grids = []
    for r in range(n):
        for c in range(n):
            grids.append((r, c))

    starts_list = []
    for row in combinations(grids, k):
        starts_list.append(row)

    return starts_list


def bfs(starts):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    visited = [[False for _ in range(n)] for _ in range(n)]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n and not visited[r][c]
    dq = deque([])

    cnt = 0
    for r, c in starts:
        dq.append((r, c))
        visited[r][c] = True
        cnt += 1

    while dq:
        cr, cc = dq.popleft()
        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            if in_range(nr, nc) and u <=  abs(board[cr][cc] - board[nr][nc]) <= d:
                dq.append((nr, nc))
                visited[nr][nc] = True
                cnt += 1

    # for row in visited:
    #     print(*row)

    return cnt

max_ans = 0
starts_list = choose_starts(k)
for starts in starts_list:
    ans = bfs(starts)
    max_ans = max(max_ans, ans)
    # print("stars: ", starts, "bfs: ", ans)

print(max_ans)