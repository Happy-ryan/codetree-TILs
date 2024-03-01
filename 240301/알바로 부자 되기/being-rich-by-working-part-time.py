# n = int(input())
# infos = [list(map(int, input().split())) for _ in range(n)]
# dp = [-1 for _ in range(n)]


# # dpf(x) 인덱스n번째 알바를 선택했을 때 내가 얻을 수 있는 최대 이익!
# # dpf(x) = max(ret, dpf(i)) + 알바값 where i알바의 끝나는 시각 < x번째 알바 시작 시간 
# def dpf(x):
#     if dp[x] != -1:
#         return dp[x]

#     ret = 0
#     is_start = True
#     for i in range(0, x):
#         if infos[i][1] < infos[x][0]:
#             ret = max(ret, dpf(i) + infos[x][2])
#             is_start = False

#     # x == 0일 때라고 하면 틀린다!!
#     # 0을 안 갈 수도 있기 때문이다!
#     # 예제2번만 봐도 index 0을 반드시 간 것은 아니다!
#     # 따라서 is_start로 판단함!
#     if is_start:
#         return infos[x][2]

#     dp[x] = ret

#     return ret 

# max_ans = 0
# for x in range(n):
#     max_ans = max(max_ans, dpf(x))
# print(max_ans)
    
n = int(input())
infos = [list(map(int, input().split())) for _ in range(n)]

# 그리디 / bfs|dfs / dp

def solution(n, infos):
    
    # dpf(x): x번째 알바를 마지막으로 선택했을 때, 얻을 수 있는 알바비의 최대값!
    # dpf(x) = max(ret, dpf(k) where 0 <= k < x and k[1] < x[0])
    dp =  [-1 for _ in range(n)]
    
    def dpf(x):
        if dp[x] != -1:
            return dp[x]
        
        ret = 0
        is_start = True
        for k in range(x):
            # 그 전에 존재하는 알바의 끝나는 시간 < 내가 마지막으로 선택한 알바의 시작시간
            if infos[k][1] < infos[x][0]:
                is_start = False
                ret = max(ret, dpf(k) + infos[x][2])
                
        if is_start:
            return infos[x][2]
                
        dp[x] = ret
        
        return ret
    
    max_money = 0
    for day in range(n):
        max_money = max(max_money, dpf(day))
    
    return max_money

print(solution(n, infos))