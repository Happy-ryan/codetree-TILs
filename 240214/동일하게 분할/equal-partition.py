n = int(input())
nums = [0] + list(map(int, input().split()))

def sol_1():
    max_m = sum(nums)
    inf = int(1e9)
    # dp[i][j] i번째 숫자를 가지고 j번째 숫자를 만들 수 있는 최소 덧셈 수
    # > 평소 풀던 동전 문제 중 중복 사용 불가 문제와 정확하게 동일하다!!
    # 왜 이걸 했어?
    # 두 집합 A = B ,,,A+B 무조건 짝수여야한다.
    # 짝수 // 2 = A = B
    # 짝수의 절반 값을 주어진 수들로 중복없이 사용했을 때 만들 수 있냐?를 판단하는 것
    # 1 100 1000 10001 의 총 합 11102이고 절반은 5551이다.
    # 주어진 숫자를 중복해서 사용하지 않으면 절대로 만들 수 없는 수이다.
    # 1 2(2)....100(1) 101(2).....
    dp = [[inf for _ in range(max_m + 1)] for _ in range(n + 1)]
    dp[0][0] = 0

    for i in range(1, n + 1):
        # 중복없이 사용..뒤에서 판단하애햠!
        for j in range(max_m, -1, -1):
            dp[i][j] = dp[i-1][j]
            if j >= nums[i]:
                dp[i][j] = min(dp[i][j], dp[i - 1][j - nums[i]] + 1)

    if max_m % 2 != 0:
        return 'No'
    else:
        target = max_m // 2
        if dp[n][target] >= inf:
            return 'No'
        else: 
            return 'Yes'

print(sol_1())