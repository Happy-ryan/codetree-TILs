from heapq import heappush, heappop

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    adj[s].append((e, cost))
    adj[e].append((s, cost))

A, B = map(int, input().split())

inf = int(1e9)
visited = [inf for _ in range(n + 1)]
prev = [0 for _ in range(n + 1)]

def bfs(start):
    
    heap = []
    heappush(heap, (0, start))
    visited[start] = 0

    while heap:
        d, cur = heappop(heap)  

        if d > visited[cur]:
            continue
        
        for nxt, nd in adj[cur]:
            if visited[nxt] > visited[cur] + nd:
                visited[nxt] = visited[cur] + nd
                prev[nxt] = cur
                heappush(heap, (visited[nxt], nxt))
    
bfs(A)

ans = []
end = B
while True:
    ans.append(end)
    end = prev[end]
    if end == 0:
        break

print(visited[B])
print(*ans[::-1])