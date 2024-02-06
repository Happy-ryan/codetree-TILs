n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < n and not visited[r][c]

def dfs(r, c):
    global cnt

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if in_range(nr, nc) and board[nr][nc] == board[r][c]:
            visited[nr][nc] = True
            cnt += 1
            dfs(nr, nc)

cnts = []
for r in range(n):
    for c in range(n):
        if visited[r][c]:
            continue
        # dfs도 시작점 체크를 미리 해야한다.
        visited[r][c] = True
        cnt = 1
        dfs(r, c)
        cnts.append((board[r][c], cnt))


max_block = 0
bomb = 0
for _, block in cnts:
    if block >= 4:
        bomb += 1
    max_block = max(max_block, block)

print(bomb, max_block)