n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n and not visited[r][c] and board[r][c] == 1


def dfs(r, c):
    global cnt
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if in_range(nr, nc):
            visited[nr][nc] = True
            cnt +=1
            dfs(nr, nc)


cnts = []
for r in range(n):
    for c in range(n):
        if board[r][c] == 0 or visited[r][c] == True:
            continue
        cnt = 0
        dfs(r, c)
        if cnt != 0:
            cnts.append(cnt)

cnts.sort()
print(len(cnts))
for x in cnts:
    print(x)