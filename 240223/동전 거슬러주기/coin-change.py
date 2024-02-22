# import sys
# sys.setrecursionlimit(10 ** 5)

# n, m = map(int, input().split())
# # 동전 중복 선택 가능
# # 동전 거슬러 주기 - dp
# coins = list(map(int, input().split()))
# inf = int(1e9)
# dp = [-1 for _ in range(m + 1)]

# # dpf(금액x) = max(ret, dpf(x - coin) + 1) where coin in coins and coin <= x
# # inf: not-visited
# # 0: impossible
# # so, dp[0] = 0? impossible?
# # dp[2] -> dp[0] -> dp[0]은 impossible이 아니다.

# # -1: not-visited
# # inf: impossible

# def dpf(money):
#     if money == 0:
#         return 0

#     if dp[money] != -1:
#         return dp[money]
        
#     # 1원으로만 전부 나눠줄 경우 최대가 된다.
#     # 최소 동전보다 작은 m은 돈을 거슬러 줄 수 없다.
#     # 1종류 1원
#     # 2원(으로 거스릴 수는 없음)
#     ret = inf
#     for coin in coins:
#         if coin <= money:
#             ret = min(ret, dpf(money - coin) + 1)

#     # 0의 의미: 동전으로 만들 수 없다.
#     # 오해하면 안되는게 money = 0이면 당연히 만들 수 없지만 0이 아니라 무조건 만들 수 있는 것도 아니다.
#     # 나에게 있는 동전이 1000원 1개 밖에 없다고 가정했을 때 10원을 어떻게 나누어주는가?
#     # 따라서 주어진 코인들보다 money가 커야한다.
#     dp[money] = ret

#     return ret

# k = dpf(m)
# if k == inf:
#     print(-1)
# else:
#     print(k)
# 동전거슬러주기
# 중복허용 / 금액 특정할 수 있음
# item: 동전 / value: 개수 / weight: 값어치
# 불가능한 경우 항상 생각하기!!
n, m = map(int, input().split())
coins = [0] + list(map(int, input().split()))
inf = int(1e9)  

def sol_1():
    # dp[i][j] i번째 동전(item)을 사용했을 때, j 값어치(weight)을 얻는 동전의 수(value)
    dp = [[inf for _ in range(m + 1)] for _ in range(n + 1)]
    
    # 동전의 수 이므로 경우의 수 아니다.
    dp[0][0] = 0
    for i in range(1, n + 1):
        v, w = 1, coins[i]
        # 중복 가능 - 앞('0', 총 금액까지)
        for j in range(0, m + 1):
            dp[i][j] = dp[i - 1][j]
            if j - w >= 0:
                dp[i][j] = min(dp[i][j], dp[i][j - w] + v)
                
    return dp[n][m]


ans = sol_1()
if ans >= inf:
    ans = -1
    
print(ans)