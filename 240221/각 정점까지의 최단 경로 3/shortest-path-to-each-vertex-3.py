from collections import deque
from heapq import heappush, heappop

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
inf = int(1e9)
in_queue = [False for _ in range(n + 1)]
visited = [inf for _ in range(n + 1)]


for _ in range(m):
    s, e, cost = map(int, input().split())
    adj[s].append((e, cost))


def bfs(cx):

    heap = []
    # (비용, 시작점cx)
    heappush(heap, (0, cx))
    visited[cx] = 0

    while heap:
        cur_dist, cur = heappop(heap)

        if cur_dist > visited[cur]:
            continue

        for nxt, add in adj[cur]:
            nxt_dist = cur_dist + add
            if visited[nxt] > nxt_dist:
                heappush(heap, (nxt_dist, nxt))
                visited[nxt] = nxt_dist
    
bfs(1)
# print(adj)
# print(in_queue)
# print(visited)

for idx in range(2, n + 1):
    ans = visited[idx]
    if ans >= inf:
        ans = -1
    print(ans)