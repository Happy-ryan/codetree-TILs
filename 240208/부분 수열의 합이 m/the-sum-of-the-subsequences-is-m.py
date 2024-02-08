# 길이(돈)가 인덱스에 매칭된다. 

# 동전 거슬러주기 - 중복 불가 유형과 유사함
# 각 숫자들을 1번씩 사용하여 특정합이 되게 하는 부분수열 중 최소 길이
# -> 몇 종류의 동전을 최대 1번씩 사용하여 x원이 되도록 할 때, 동전의 수를 최소로 써주세요!
# -1: not-visited 
# inf: impossible > 만들 수 없는 길이(돈)
# 동전문제도 dp의 정의를 살펴보면 지금까지 선택한 동전의 합이 i라고 했을 때, 가능한 최소 동전의 개수
# dpf(length):  부분 수열의 길이가 Length라고 했을 때, 가능한 최소 부분수열의 길이
# dpf(length) = min(ret, dpf(length - x) + 1)
#               where x <= length
#               where x in numbers
# 거꾸로 생각하면 수열의 원소 또는 동전이 중복되게 선택되지 않는다.

n, m = map(int, input().split())
# dp[0][0] 이 나오도록 하기 위해서 coins에 [0] 추가
coins = [0] + list(map(int, input().split()))

inf = int(1e9)

dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]

# dpf(i, j): i번째 코인을 사용해서 j금액을 만든다!
# dpf(i, j) = dpf(i - 1, j)(i번째 coin 안사용한 경우) + dpf(i - 1, j - coin[i])
# -1 방문을 안함 / 0 불가능
def dpf(i, j):
    if i == 0:
        if j == 0:
            return 1
        else:
            return 0
    if j < 0:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]
    
    
    ret = dpf(i - 1, j) + dpf(i - 1, j - coins[i])

    dp[i][j] = ret

    return ret

ans = dpf(n, m)

if ans == 0:
    ans = -1

print(ans)
    


# # # 2
# # # [-1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2]
# # # 틀린이유: 같은 동전이 중복돼서 사용되고 있음. dpf(12) = 2(가지) = 6(1가지) + 6(1가지)
# n, m = map(int, input().split())
# numbers = list(map(int, input().split()))

# inf = int(1e9)

# dp = [inf for _ in range(m + 1)]
# dp[0] = 0
# for i in range(n):
#     for j in range(m, -1, -1):
#         if j >= numbers[i]:
#             if dp[j - numbers[i]] == inf:
#                 continue
#             dp[j] = min(dp[j], dp[j - numbers[i]] + 1)

# ans = dp[m]
# if ans == inf:
#     ans = -1
# print(ans)