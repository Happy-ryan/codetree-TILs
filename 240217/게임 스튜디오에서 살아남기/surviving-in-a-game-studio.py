n = int(input())
mod = int(1e9) + 7
dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n + 1)]
# 3^1000 문자 자체를 만드는건 하수!!
# dp[i][j][k] = i번을 반드시 선택했을 때, B의 연속한 개수j,  T의 개수 k인 평가 경우의 수
# dp[i][j][k] = (if j == 0 > G 선택) dp[i - 1][j][k]
#             = (if j == 1 or j== 2 > B 선택) dp[i - 1][j - 1][k]
#             = (if  T 선택) dp[i - 1][j][k - 1]
 
dp[0][0][0] = 1
for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):
            if j == 0:
                # BBBBG
                # G가 붙으면 j == 0이 된다.
                # 따라서 연속된 B의 개수 0 ~ 2개 상태 모두에 G붙일 수 있다.
                for z in range(3):
                    dp[i][j][k] += dp[i - 1][z][k]
                    dp[i][j][k] %= mod
            elif j == 1 or j == 2:
                dp[i][j][k] += dp[i - 1][j - 1][k]
                dp[i][j][k] %= mod
            if j == 0 and k - 1 >= 0:
                for z in range(3): 
                    dp[i][j][k] += dp[i - 1][z][k - 1]
                    dp[i][j][k] %= mod

# 합치고도 mod하기!!!
print(sum(dp[n][0] + dp[n][1] + dp[n][2]) % mod)