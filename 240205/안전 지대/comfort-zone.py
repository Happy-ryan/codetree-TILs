import sys
sys.setrecursionlimit(10**5)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]


def in_range(r, c):
    return 0 <= r < n and 0 <= c < m and not visited[r][c]

def dfs(r, c, k):
    global cnt
    global visited
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if in_range(nr, nc) and board[nr][nc] > k:
            visited[nr][nc] = True
            cnt += 1
            dfs(nr, nc, k)


# 시작점이 없는 유형, 높이도 안정해짐
ans = []
for k in range(1, 100):
    cnts = []
    # 전부 방문하고 올때마다 visted를 초기화해야한다
    visited = [[False for _ in range(m)] for _ in range(n)]
    for r in range(n):
        for c in range(m):
            if board[r][c] <= k or visited[r][c] == True:
                continue
            visited[r][c] = True
            cnt = 1
            dfs(r, c, k)
            cnts.append(cnt)
    ans.append((k, len(cnts)))

ans.sort(key=lambda x: (-x[1], x[0]))

print(*ans[0])