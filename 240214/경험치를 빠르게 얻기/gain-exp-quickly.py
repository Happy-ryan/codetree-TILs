n, m = map(int, input().split())
infos = [0] + [list(map(int, input().split())) for _ in range(n)]

def sol_1():
    # 보통은 dp[i][j] i번째 퀘스트를 했을 때의 경험치j를 만들기 위한 최소 시간(값)
    # 그래서 가방의 문제의 경우, 가방의무게에 무게의 한도를 둔다. 동전의 문제의 경우에도 목표되는 동전 금액 즉, 한도가 있다.
    # 그런데 이 문제의 문제는 경험치를 한도를 알 수가 없다. 그러다보니 열이 매우매우 커질 수 있고 메모리 초과!!!
    # 그래서 이번에는 dp[i][j] i번째 퀘스트를 했을 때 시간(j) 만들기 위한 최대 경험치(값)
    t = 100
    inf = int(1e9)
    dp = [[-inf for _ in range(t + 1)] for _ in range(n + 1)]
    
    dp[0][0] = 0
    for i in range(1, n + 1):
        # 동전(v-개수(값), w-원) / 배낭(v-가치(값), w-무게) 
        # 값 >> dp에 들어갈 애들!!
        v, w = infos[i]
        for j in range(t, -1, -1):
            dp[i][j] = dp[i - 1][j]
            if j - w >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - w] + v)

    min_time = 101
    for idx, exp in enumerate(dp[n]):
        if m <= exp:
            min_time = min(min_time, idx)
    # 불가능한 경우 항상 생각하기!!!
    ans = min_time
    if ans >= 101:
        ans = -1
    return ans


print(sol_1())