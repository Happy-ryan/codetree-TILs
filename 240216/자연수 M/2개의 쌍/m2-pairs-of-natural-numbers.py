# 두 집합의 차이가 적은 것을 찾아야함
# 8 7 6 2
# (최대, 최소)로 구성
# 총합을 m/2로 만들어야하는데 최대값이 최소를 만들기 위해서 최대, 최소로 구성해서 각 쌍의 차이를 최소화 시키는게 최대화를 시킬 수 있을 것 같음

from collections import deque

t = int(input())

arr = []
for _ in range(t):
    x, y = map(int, input().split())
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

    #  쌍을 이룰 수 있는 경우 쌍의 개수만큼 제거!
    # (2, 8) - (4, 1) 이라고 했을 때 최대2개까지 생성 가능하므로 min(2, 4)만큼 제거
    # 문제는 dq에 숫자 종류가 1개만 남을 경우 남은 숫자 * 2만 해도 된다. 어짜피 2 * 숫자만 나올 것이므로!
    if len(dq) == 1:
        ans = max(ans, dq[first][1] * 2)
        break

    ans = max(ans, dq[first][1]+ dq[last][1])
    k = min(dq[first][0], dq[last][0])
    dq[first][0] -= k
    dq[last][0] -= k

print(ans)