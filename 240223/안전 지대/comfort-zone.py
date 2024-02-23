# import sys
# sys.setrecursionlimit(10**5)

# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]


# def in_range(r, c):
#     return 0 <= r < n and 0 <= c < m and not visited[r][c]

# def dfs(r, c, k):
#     global cnt
#     global visited
#     dr = [-1, 1, 0, 0]
#     dc = [0, 0, -1, 1]
    
#     for d in range(4):
#         nr = r + dr[d]
#         nc = c + dc[d]
#         if in_range(nr, nc) and board[nr][nc] > k:
#             visited[nr][nc] = True
#             cnt += 1
#             dfs(nr, nc, k)


# # 시작점이 없는 유형, 높이도 안정해짐
# ans = []
# for k in range(1, 100):
#     cnts = []
#     # 전부 방문하고 올때마다 visted를 초기화해야한다
#     visited = [[False for _ in range(m)] for _ in range(n)]
#     for r in range(n):
#         for c in range(m):
#             if board[r][c] <= k or visited[r][c] == True:
#                 continue
#             visited[r][c] = True
#             cnt = 1
#             dfs(r, c, k)
#             cnts.append(cnt)
#     ans.append((k, len(cnts)))

# ans.sort(key=lambda x: (-x[1], x[0]))

# print(*ans[0])

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

def solution():
    global cnt
    
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    
    def in_range(r, c):
        return 0 <= r < n and 0 <= c < m
    
    def dfs(r, c):
        global cnt
        for k in range(4):
            nr, nc = r + dr[k], c + dc[k]
            if in_range(nr, nc) and board[nr][nc] > high and not visited[nr][nc]:
                cnt += 1
                visited[nr][nc] = True
                dfs(nr, nc)
        
    ans = []
    # 높이에 대해서 브루트포스
    for high in range(1, 101):
        # 새로운 높이일 때마다 cnts와 visted 초기화
        cnts = []
        visited = [[False for _ in range(m)] for _ in range(n)]
        for r in range(n):
            for c in range(m):
                if visited[r][c] or board[r][c] <= high:
                    continue
                cnt = 1
                dfs(r, c)
                cnts.append(cnt)
        ans.append((high, len(cnts)))
        
    ans.sort(key=lambda x: (-x[1], x[0]))
    return (ans[0][0], ans[0][1])


print(*solution())