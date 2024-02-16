# 두 집합의 차이가 적은 것을 찾아야함
# 8 7 6 2
# (최대, 최소)로 구성
# 총합을 m/2로 만들어야하는데 최대값이 최소를 만들기 위해서 최대, 최소로 구성해서 각 쌍의 차이를 최소화 시키는게 최대화를 시킬 수 있을 것 같음

from collections import deque

t = int(input())

m = 0
arr = []
for _ in range(t):
    x, y = map(int, input().split())
    m += x  
    arr.append([x, y])
# 값으로 정렬, 오름차순
arr.sort(key=lambda x: x[1])
dq = deque(arr)

first = 0
last = -1
ans = 0
while dq:
    if dq[first][0] == 0:
        dq.popleft()

    if not dq:
        break

    if dq[last][0] == 0:
        dq.pop()

    if dq[first][0] != 0 and dq[last][0] != 0:
        # print(f"{dq[first][1]} + {dq[last][1]}")
        ans = max(ans, dq[first][1]+ dq[last][1])
        dq[first][0] -= 1
        dq[last][0] -= 1


print(ans)