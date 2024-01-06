N, M = map(int, input().split())
adj = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    s, e = map(int, input().split())
    adj[s].append(e)
    adj[e].append(s)

visited[1] = True
cnt = 0
def dfs(start):
    global cnt
    for cur in adj[start]:
        if not visited[cur]:
            cnt += 1
            visited[cur] = True
            dfs(cur)
dfs(1)
print(cnt)