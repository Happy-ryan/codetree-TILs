# 토마토 문제와 유사 
# 시뮬레이션 + bfs
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def in_range(r, c):
    # n, m 다를 때 주의
    return 0 <= r < n and 0 <= c < m

# 가장 바깥에 존재하는 빙하들을 찾는 함수!
def find_outside_water():
    outside_ice = []
    in_queue = [[False for _ in range(m)] for _ in range(n)]

    dq = deque([])
    for start in [(0, 0)]:
        r, c = start
        dq.append((r, c))
        in_queue[r][c] = True
        outside_ice.append((r, c))

    while dq:
        cr, cc = dq.popleft()
        for k in range(4):
            nr = cr + dr[k]
            nc = cc + dc[k]
            if in_range(nr, nc) and not in_queue[nr][nc] and board[nr][nc] == 0:
                dq.append((nr, nc))
                in_queue[nr][nc] = True
                outside_ice.append((nr, nc))

    return outside_ice


def simulate():
    outside_water = find_outside_water()
    # 변한 것의 갯수
    cnt = 0
    for ice in outside_water:
        i, j = ice
        for k in range(4):
            n_i, n_j = i + dr[k], j + dc[k]
            if in_range(n_i, n_j) and board[n_i][n_j] == 1:
                board[n_i][n_j] = 0
                cnt += 1
    
    return cnt

t = 0
ans = 0
while True:
    cnt = simulate()
    if cnt == 0:
        break
    t += 1
    ans = cnt

print(t, ans)