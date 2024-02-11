# "최소" 연산 횟수 > dp - 그래프 탐색 - 그리디 순...

from collections import deque

n = int(input())
in_queue = {}
dist = {}

def bfs(n):
    dq = deque([])

    dq.append(n)
    dist[n] = 0
    in_queue[n] = True

    while dq:
        cur = dq.popleft()

        num_list = [cur + 1,cur - 1]
        if cur % 2 == 0:
            num_list.append(cur // 2)
        if cur % 3 == 0:
            num_list.append(cur // 3)

        if 1 not in num_list:
            for nxt in num_list:
                # -1이 존재해서 기존에 갔던 것으로 되돌아 갈 수 있음.
                # in_queue에 없다는 것을 확인한 후에 bfs 돌기 가능!
                if nxt not in in_queue:
                    dq.append(nxt)
                    in_queue[nxt] = True
                    dist[nxt] = dist[cur] + 1
        else:
            dist[1] = dist[cur] + 1
            break
    print(dist[1])

bfs(n)