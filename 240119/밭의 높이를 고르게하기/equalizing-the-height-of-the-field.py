N, H, T = map(int, input().split())

highs = list(map(int, input().split()))

# 핵심: 특정 구간 내(T길이)에서 구간 내의 높이가 H높이로 일정하게 만들기 위한 최소의 비용을 찾으세요.
# 구간의 설정을 위해서 양끝점! 
# 양끝점이 설정되었을 때 H로 만들기 위한 비용

def cal(row):
    cost = 0
    for h in row:
        cost += abs(h - T)
    return cost

min_cost = 10000000
for i in range(0, N - T + 1):
    cost = 0
    for j in range(i, i + T):
        cost += abs(highs[j] - T)
    min_cost = min(min_cost, cost)

print(min_cost)