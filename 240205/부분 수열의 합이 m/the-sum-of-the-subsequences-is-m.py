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
def dpf(length: int):
    if length == 0:
        return 0

    if dp[length] != -1:
        return dp[length]
    # target_length = 12
    # [2, 5, 10]
    # 12 - 10 = 2 not in numbers 
    # dpf(2) 만들 수가 없음!! -> inf!
    # 각 원소를 1개씩만 쓰도록 만들어야함!
    ret = inf
    for x in numbers: 
        if x <= length:
            ret = min(ret, dpf(length - x) + 1)

    dp[length] = ret

    return ret


# # 2
# # [-1, 1, 1, 2, 1, 1, 1, 2, 2, 2, 2, 2, 2]
# # 틀린이유: 같은 동전이 중복돼서 사용되고 있음. dpf(12) = 2(가지) = 6(1가지) + 6(1가지)
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

inf = int(1e9)

dp = [inf for _ in range(m + 1)]
dp[0] = 0
for i in range(n):
    for j in range(m, -1, -1):
        if j >= numbers[i]:
            if dp[j - numbers[i]] == inf:
                continue
            dp[j] = min(dp[j], dp[j - numbers[i]] + 1)

ans = dp[m]
if ans == inf:
    ans = -1
print(ans)