# bfs + 완탐(치울 돌 결정하는 부분)
# 완탐: O(8Cm) --- max(8C4)
from collections import deque
from itertools import combinations

n, k, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
starts = [list(map(int, input().split())) for _ in range(k)]


def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    in_queue = [[False for _ in range(n)] for _ in range(n)]

    def in_range(r, c):
        return 0 <= r < n and 0 <= c < n and not in_queue[r][c] and board[r][c] == 0

    dq = deque([])

    cnt = 0
    for r, c in starts:
        r -= 1
        c -= 1
        dq.append((r , c))
        in_queue[r][c] = True;
        cnt += 1


    while(dq):
        cr, cc = dq.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if in_range(nr, nc):
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                cnt += 1
    return cnt

def find_stone_pos():
    pos = []
    for r in range(n):
        for c in range(n):
            if board[r][c] == 1:
                pos.append((r, c))
    return pos

max_val = 0
pos = find_stone_pos()
for row in combinations(pos, m):
    # 1 -> 0 으로 변경
    for r, c in row:
        board[r][c] = 0
    max_val = max(max_val, bfs())
    # 0 -> 1로 원상복귀
    for r, c in row:
        board[r][c] = 1

print(max_val)