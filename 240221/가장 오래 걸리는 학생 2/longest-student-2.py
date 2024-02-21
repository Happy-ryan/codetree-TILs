# n개의 서로 장소 / 1 ~ (n - 1번) 학생 한명 / n번 학교
# 방향성
# 최단이동거리 이동
# 거리 1 이동하는 데 1초의 시간
# 1 ~ n - 1번 학생이 n번으로 갈 때 가장 오래 걸리는 사람
# 답이 없는 경우
from heapq import heappush, heappop

n, m = map(int, input().split())
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    e, s, cost = map(int, input().split())
    adj[s].append((cost, e))

inf = int(1e9)
visited = [inf for _ in range(n + 1)]

def bfs(start):

    heap = []
    heappush(heap, (0, start))
    visited[start] = 0

    while heap:
        d, cur = heappop(heap)

        if d > visited[cur]:
            continue

        for nd, nxt in adj[cur]:
            if visited[nxt] > visited[cur] + nd:
                visited[nxt] = visited[cur] + nd
                heappush(heap, (visited[nxt], nxt))

bfs(n)
max_ans = 0
for idx in range(1, n + 1):
    max_ans = max(max_ans, visited[idx])
    
print(max_ans)