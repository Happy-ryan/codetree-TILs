from heapq import heappush, heappop

n, m = map(int, input().split())
k = int(input())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, cost = map(int, input().split())
    adj[s].append((cost, e))
    adj[e].append((cost, s))

inf = int(1e9)
visited = [inf for _ in range(n + 1)]

def bfs(start):
    
    heap = []
    # 힙정렬 (비용, 위치)
    heappush(heap, (0, start))
    visited[start] = 0
    # print("start: ", start)
    while heap:
        d, cur = heappop(heap)
        # print("d, cur:", d, cur)
        # print("visited[cur]:", visited[cur])
        if d > visited[cur]:
            continue

        for nd, nxt in adj[cur]:
            # print("nd, nxt:", nd, nxt)
            # print("visited[nxt]:", visited[nxt])
            if visited[nxt] > visited[cur] + nd:
                visited[nxt] = visited[cur] + nd
                heappush(heap, (visited[nxt], nxt))

bfs(k)

for idx in range(1, n + 1):
    ans = visited[idx]
    if ans >= inf:
        ans -= 1
    print(ans)