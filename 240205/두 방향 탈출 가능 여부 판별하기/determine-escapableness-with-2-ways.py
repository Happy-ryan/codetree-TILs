n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

dr = [1, 0]
dc = [0, 1]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m


visited[0][0] = True
cnt = 0

def dfs(r, c):
    global cnt
    for k in range(2):
        nr = r + dr[k]
        nc = c + dc[k]
        if in_range(nr, nc) and not visited[nr][nc] and board[nr][nc] == 1:
            visited[nr][nc] = True
            cnt +=1 
            dfs(nr, nc)

dfs(0, 0)

if visited[n - 1][m - 1]:
    print(1)
else:
    print(0)