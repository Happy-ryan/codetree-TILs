# k개를 하나를 n번 선택하기 -> 순열을 의미
# 순열에 조건이 없음 - simple / 순열에 조건이 있음 - conditional

# 조건: 연속하여 같은 숫자 3번이상은 제외 

k, n = map(int, input().split())

ans = []
def dfs(level):
    if level == n:
        print(*ans)
        return         
    
    for cur_number in range(1, k + 1):
        # [x] [cur_number] [cur_number] > ok
        # [cur_number] [x] [cur_number] > ok
        # [x] [x] [cur_number] > ok
        # [cur_number] [cur_number] [cur_number] > 제외
        # 길이가 2이상부터 3연속의 경우가 발생할 수 있다. 그 전에 -1, -2 체크하면 인덱스 에러 난다.
        if len(ans) < 2 or (len(ans) >= 2 and (ans[-1] != cur_number or ans[-2] != cur_number)):
            ans.append(cur_number)
            dfs(level + 1)
            ans.pop()


dfs(0)