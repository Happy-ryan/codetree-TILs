# 직사각형의 크기는 매우 다양함...
# 총 사각형의 수는 nC2 * nC2 = 300C2 * 300C2 = 20억..// 2개의 좌표가 필요함.
# 각 사각형의 합: 보통 n^2
# 따라서 사각형을 구할 때마다 사각형의 합을 구하게 되면 n^4으로 시간초과 발생함
# 따라서 사각형 전수를 보는건 무조건 발생하므로 사각형의 합에서 시간을 줄여야한다
# 이 방법이 바로 누적합을 이용하는 것이다.
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
psum = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        psum[i + 1][j + 1] = board[i][j] + psum[i + 1][j] + psum[i][j + 1] - psum[i][j]

def range_sum(r1, c1, r2, c2):
    return psum[r2 + 1][c2 + 1] - psum[r2 + 1][c1] - psum[r1][c2 + 1] + psum[r1][c1]


ans = -1000 * 300 * 300
for r1 in range(n):
    for c1 in range(n):
        for r2 in range(r1, n):
            for c2 in range(c1, n):
                ans = max(ans, range_sum(r1, c1, r2, c2))

print(ans)