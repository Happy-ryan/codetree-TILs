# n 20밖에 안되므로 누적합을 할 필요도 없긴 하지만..
# 나는 누적합을 사용해서 풀어보겠다!!
# 사각형의 크기를 물어봤다. 합이 아니므로 누적합 문제는 아니다.
# 완전탐색 문제이다.

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

psum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

for r in range(n):
    for c in range(m):
        psum[r + 1][c + 1] = board[r][c] + psum[r + 1][c] + psum[r][c + 1] - psum[r][c]

def range_sum(r1, c1, r2, c2):
    return psum[r2 + 1][c2 + 1] - psum[r2 + 1][c1] - psum[r1][c2 + 1] + psum[r1][c1]

def check(r1, c1, r2, c2):
    for r in range(r1, r2 + 1):
        for c in range(c1, c2 + 1):
            if board[r][c] < 0:
                return False
    return True

max_ans = 0
for r1 in range(n):
    for c1 in range(n):
        for r2 in range(r1, n):
            for c2 in range(c1, n):
                if check(r1, c1, r2, c2):
                    max_ans = max(max_ans, (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1))

if max_ans == 0:
    max_ans = -1

print(max_ans)