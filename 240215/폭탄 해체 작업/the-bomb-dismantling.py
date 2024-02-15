# 시간대비 점수가 높은 애를 먼저 선택하는게 항상 이득이 되냐?
# 8/1(8), 2/1(2), 10/3(3.xx), 7/5(1.xx)
# 1초 박에 안걸림!! 1초 선택해서 해체해도 2초 것도 해체 가능!!
# 같은 초에 있으면 점수 큰거..!
from heapq import heappush, heappop

t = int(input())
bombs = [list(map(int, input().split())) for _ in range(t)]
bombs.sort(key= lambda x: (x[1], x[0]))
MAX_TIME = bombs[-1][-1]

bomb_list = [[] for _ in range(MAX_TIME + 1)]
for score, limit in bombs:
    bomb_list[limit].append(score)

heap = []
cnt = 0
for time in range(MAX_TIME, 0, -1):
    for score in bomb_list[time]:
        heappush(heap, -score)
    if len(heap) == 0:
        continue
    q = -heappop(heap)
    cnt += q
    
print(cnt)