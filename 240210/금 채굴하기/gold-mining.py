n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dr = [-1, 1, 0, 0]
dc = [0 , 0, -1, 1]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 좌표(0, 0) 기준 거리가 k인 점들의 집합
def taxi_circle(k):
    if k == 0:
        return [(0, 0)]
    # 거리가 k라는 것은 x좌표 + y좌표 = k 가 됨을 의미한다.
    points = []
    # 축 - 양, 음
    points.append((k, 0))
    points.append((-k, 0))
    points.append((0, k))
    points.append((0, -k))
    # 1사분면 - 2사분면
    for i in range(1, k):
        points.append((i, k - i))
        points.append((i, -(k - i)))
    # 3 - 4 사분면
    for i in range(1, k):
        points.append((-i, k - i))
        points.append((-i, -(k - i)))

    return points


# k는 거리르 의미함. 최대 거리는 얼마가 될 수 있을까?
# n = 5  >> max_k = 8
max_k = 2 * (n - 1)

delta = []
for i in range(0, max_k + 1):
    delta.append(taxi_circle(i))
    
ans = 0
for r in range(n):
    for c in range(n):
        gold_cnt = 0
        for k in range(0, max_k + 1):
            for dr, dc in delta[k]:
                nr = r + dr
                nc = c + dc
                if in_range(nr, nc) and board[nr][nc] == 1:
                    gold_cnt += 1
                if gold_cnt * m > k * k + (k + 1) * (k + 1):
                    ans = max(ans, gold_cnt)

print(ans)