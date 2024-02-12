n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]
dp = [-1 for _ in range(n)]


# dpf(x) 인덱스n번째 알바를 선택했을 때 내가 얻을 수 있는 최대 이익!
# dpf(x) = max(ret, dpf(i)) + 알바값 where i알바의 끝나는 시각 < x번째 알바 시작 시간 
def dpf(x):
    if dp[x] != -1:
        return dp[x]

    ret = 0
    is_start = True
    for i in range(0, x):
        if infos[i][1] < infos[x][0]:
            ret = max(ret, dpf(i) + infos[x][2])
            is_start = False

    if is_start:
        return infos[x][2]

    dp[x] = ret

    return ret 

max_ans = 0
for x in range(n):
    max_ans = max(max_ans, dpf(x))
print(max_ans)