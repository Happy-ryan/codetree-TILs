n, m = map(int, input().split())
infos = [0] + [list(map(int, input().split())) for _ in range(n)]

def sol_1():
    # dp[i][j] i번 보석을 선택했을 때 j무게를 달성하는 '가치'
    # 가치 - 동전의 개수 // 무게 - 동전의 원
    inf = int(1e9)
    dp = [[ -inf for _ in range(m + 1)] for _ in range(n + 1)]

    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(m, -1, -1):
            dp[i][j] = dp[i - 1][j]
            if j - infos[i][0] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - infos[i][0]] +  infos[i][1])


    return max(dp[n])

print(sol_1())