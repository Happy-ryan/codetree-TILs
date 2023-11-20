from collections import deque

n, k = map(int, input().split())
q = deque(list(range(1, n + 1)))

while q:
    for _ in range(k-1):
        # k번째가 나오기 전까지는 앞에서 빼서(popleft) 뒤에 넣음(append)
        num = q.popleft()
        q.append(num)
    # k번째 popLeft로 출력하기
    print(q.popleft(), end=" ")