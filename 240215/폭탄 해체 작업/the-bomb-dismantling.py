# 시간대비 점수가 높은 애를 먼저 선택하는게 항상 이득이 되냐?
# 8/1(8), 2/1(2), 10/3(3.xx), 7/5(1.xx)
# 1초 박에 안걸림!! 1초 선택해서 해체해도 2초 것도 해체 가능!!
# 같은 초에 있으면 점수 큰거..!
MAX_TIME = 10001
dp = [0] * MAX_TIME
t = int(input())
for _ in range(t):
    score, time = map(int, input().split())
    dp[time] = max(dp[time], score)

print(sum(dp))