# 동전 문제 중 동전끼리 배수가 아닌 경우의 그리디!
# 그리디, dp도 가능해보임
# 동전 자체를 중복사용가능하기때문에 dp 쉬운 유형
import sys
sys.setrecursionlimit(10**5)

inf = int(1e9)

money = int(input())
dp = [-1 for _ in range(money + 1)]

def dpf(money):
    if dp[money] != -1:
        return dp[money]

    if money == 0:
        return 0

    ret = inf
    is_start = True
    for x in [2, 5]:
        if x <= money:
            ret = min(ret, dpf(money - x) + 1)
            is_start = False
    # 1원..
    # inf 불가능!
    if is_start:
        return inf

    dp[money] = ret

    return ret


ans = dpf(money)
if ans >= inf:
    ans = -1

print(ans)