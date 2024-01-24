# 출발지가 2개 이상인 문제

from collections import deque

n, k = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]
in_queue = [[False for _ in range(n)] for _ in range(n)]

starts = [list(map(int, input().split())) for _ in range(k)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n and not in_queue[r][c] and board[r][c] == 0


def bfs():

    cnt = 0
    dq = deque([])

    for r, c in starts:
        r -= 1
        c -= 1
        dq.append((r, c))
        in_queue[r][c] = True
        cnt += 1


    while dq:
        cr, cc = dq.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if in_range(nr, nc):
                in_queue[nr][nc] = True
                dq.append((nr, nc))
                cnt += 1
    
    return cnt

print(bfs())