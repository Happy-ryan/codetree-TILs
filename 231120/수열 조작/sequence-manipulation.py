from collections import deque
n = int(input())
dq = deque(list(range(1, n + 1)))

while len(dq) != 1:
    # 맨 앞의 정수 제거
    dq.popleft()
    # 그 후 남은 수열의 맨 앞의 정수 맨 뒤로 이동
    dq.append(dq.popleft())

print(*dq)