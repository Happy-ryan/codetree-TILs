# 세로1, 가로3 - 회전 불가능!!
# 반드시 누운 상태로만 2개 넣어야함!
# 세로줄 고르기 nC2
# 가로줄 고르기 n - 2

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

def get_row_max_coin(r: int):
    cnt = 0
    for col in range(0, n - 2):
        one_block = board[r][col : col + 3]
        cnt = max(cnt, one_block.count(1))
    
    return cnt

from itertools import combinations

def solution():
    max_coin_count = 0
    for x, y in combinations(range(n), 2):  
        max_coin_count = max(max_coin_count, get_row_max_coin(x) + get_row_max_coin(y))

    return max_coin_count


print(solution())