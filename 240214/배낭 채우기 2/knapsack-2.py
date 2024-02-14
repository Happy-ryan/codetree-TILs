n, m = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(n)]

def sol_1():
    inf = int(1e9)
    # dp[i] = i무게를 달성했을 때의 가치가 기록이된다!!
    # 중복 사용 가능 -> 앞에서부터 보자!
    dp = [-inf for _ in range(m + 1)]
    # 
    dp[0] = 0
    for w, v in infos:
        for i in range(1, m + 1):
            if w <= i:
                dp[i] = max(dp[i], dp[i - w] + v)
    return max(dp)

print(sol_1())