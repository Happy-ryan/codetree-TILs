n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

k = 3
# 사각형의 기준 - 왼쪽 상단의 꼭지점
def check(cr, cc):
    cnt = 0
    for r in range(cr, cr + k):
        for c in range(cc, cc + k):
            if board[r][c] == 1:
                cnt += 1
    return cnt

ans = 0
for r in range(n):
    for c in range(n):
        if r + 2 >= n or c + 2 >= n:
            continue

        ans = max(ans, check(r, c))

print(ans)