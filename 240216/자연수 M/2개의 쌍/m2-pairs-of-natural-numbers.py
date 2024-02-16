# 두 집합의 차이가 적은 것을 찾아야함
# 8 7 6 2
# (최대, 최소)로 구성
# 총합을 m/2로 만들어야하는데 최대값이 최소를 만들기 위해서 최대, 최소로 구성해서 각 쌍의 차이를 최소화 시키는게 최대화를 시킬 수 있을 것 같음

from heapq import heappush, heappop
from collections import Counter
max_heap = []
min_heap = []

t = int(input())
dic = Counter()
m = 0
for _ in range(t):
    x, y = map(int, input().split())
    m += x
    heappush(max_heap, -y)
    heappush(min_heap, y)
    dic[y] = x

ans = 0
for _ in range(m // 2):
    max_q = -heappop(max_heap)
    min_q = heappop(min_heap)
    # q에 10억개를 모두 넣을 수는 없으므로
    # dic로 사용회수를 체크한다.
    # 최대, 최소값의 사용회수가 0이 되기 전까지는 pop한다음에 다시 push를 해줘야한다!!
    if dic[max_q] != 0:
        heappush(max_heap, -max_q)
        dic[max_q] -= 1
    if dic[min_q] != 0:
        heappush(min_heap, min_q)
        dic[min_q] -= 1

    # print(f"max: {max_q}, min: {min_q}")
    ans = max(ans, max_q + min_q)

print(ans)