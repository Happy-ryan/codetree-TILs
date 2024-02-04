n, m = map(int, input().split())
# 동전 중복 선택 가능
# 동전 거슬러 주기 - dp
coins = list(map(int, input().split()))
inf = int(1e8)
dp = [inf for _ in range(m + 1)]

# dpf(금액x) = max(ret, dpf(x - coin) + 1) where coin in coins and coin <= x
def dpf(money):
    if dp[money] != inf:
        return dp[money]
        
    # 1원으로만 전부 나눠줄 경우 최대가 된다.
    # 최소 동전보다 작은 m은 돈을 거슬러 줄 수 없다.
    # 1종류 1원
    # 2원(으로 거스릴 수는 없음)
    ret = money // 1
    is_possible = False
    for coin in coins:
        if coin <= money:
            ret = min(ret, dpf(money - coin) + 1)
            is_possible = True;

    # 0의 의미: 동전으로 만들 수 없다.
    # 오해하면 안되는게 money = 0이면 당연히 만들 수 없지만 0이 아니라 무조건 만들 수 있는 것도 아니다.
    # 나에게 있는 동전이 1000원 1개 밖에 없다고 가정했을 때 10원을 어떻게 나누어주는가?
    # 따라서 주어진 코인들보다 money가 커야한다.
    if not is_possible:
        return 0
    
    dp[money] = ret

    return ret

k = dpf(m)
if k == 0:
    print(-1)
else:
    print(k)