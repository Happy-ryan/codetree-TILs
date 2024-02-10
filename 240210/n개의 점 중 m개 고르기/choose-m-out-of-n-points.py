from itertools import combinations

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

def dist(x1, y1, x2, y2):
    return (x2 - x1) ** 2 + (y2 - y1) ** 2

# 두 점 사이의 거리는 완탐을 돌리자 > 최대 20C10 = 184756 > 시간초과 걸리겠는데..?
# nCm * mC2 = 20C10 * 10C2 
def cal(ans):
    max_val = 0
    for p1, p2 in combinations(ans, 2):
        max_val = max(max_val, dist(p1.x, p1.y, p2.x, p2.y))
    return max_val


n, m = map(int, input().split())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append(Point(x, y))

ans = []
final_ans = 10000
def combination(cur_idx, cnt):
    global final_ans
    if cur_idx == n:
        if cnt == m:
            final_ans = min(final_ans, cal(ans))
        return

    ans.append(points[cur_idx])
    combination(cur_idx + 1, cnt + 1)
    ans.pop()

    combination(cur_idx + 1, cnt)

combination(0, 0)
print(final_ans)