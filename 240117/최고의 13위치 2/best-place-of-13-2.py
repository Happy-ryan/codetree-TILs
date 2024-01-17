# 세로1, 가로3 - 회전 불가능!!
# 반드시 누운 상태로만 2개 넣어야함!
# n이 커지면 한줄에 2개를 넣을 수도 있다!
# 세로줄 고르기 nC2
# 가로줄 고르기 n - 2

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 완탐을 돌리자..! 겹치지않는다가 포인트!
# 가장 왼쪽 사각형이 기준
def get_max_coin(cr, cc):
    ans = 0
    cnt = board[cr][cc : cc + 3].count(1)
    for i in range(n):
        for j in range(n - 2):
            # 겹치지 않기 위해서는 j기준 양쪽을 모두 봐야한다!
            if (i == cr and (cc <= j <= cc + 2)) or (i == cr and (cc - 2 <= j <= cc)):
                continue
            k = board[i][j : j + 3].count(1)
            ans = max(ans, cnt + k)
    return ans


ans = 0
for cr in range(n):
    for cc in range(n - 2):
        coin_count = get_max_coin(cr, cc)
        ans = max(ans, coin_count)

print(ans)



# n이 커지면 한줄에 2개를 넣을 수도 있다! <- 틀린 이유