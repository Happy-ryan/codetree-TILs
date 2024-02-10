n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 격자 안에서 단일 객체의 이동 + 시계 & 반시계 90도 회전이 있는 문제!
# 회전 - 동(0) 남(1) 서(2) 북(3)
# 반시계 - 시계가 정확하게 나뉘어지는게 아님!!
# /: 동(0) -> 북(3)-반시계|| 북(3) -> 동(0)-시계
# /: 남(1) -> 서(2)-시계 || 사(2) -> 남(1)-반시계
# \: 동(0) -> 남(1)-시계 || 남(1) -> 동(0)-반시계

def change_dir(r, c, d):
    if board[r][c] == 1:
        if d == 0:
            d = 3
        elif d == 1:
            d = 2
        elif d == 2:
            # 틀린이유!
            d = 1
        elif d == 3:
            d = 0
    elif board[r][c] == 2:
        if d == 0:
            d = 1
        elif d == 1:
            d = 0
        elif d == 2:
            d = 3
        elif d == 3:
            d = 2
    else:
        d = d

    return d


# [1 - /] 반시계방향 (cur + 1) % 4
# [2 - \] 시계방향 (cur + 3) % 4
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def in_range(r, c):
    return 0 <= r < n and 0 <= c < n

# 1초동안 움직임을 의미하는 함수
def simulate(r, c, d):

    d = change_dir(r, c, d)
    
    nr = r + dr[d]
    nc = c + dc[d]

    return nr, nc, d

check = []
for col in range(n):
    check.append((0, col, 1))
    check.append((n - 1, col, 3))
for row in range(n):
    check.append((row, 0, 0))
    check.append((row, n - 1, 2))

max_ans = 0
for r, c, d in check:
    t = 2
    # print(f"초입 - r: {r},c: {c}, d: {d}, t: {t}")
    while True:
        r, c, d = simulate(r, c, d)
        if not in_range(r, c):
            break
        else:
            t += 1
            # print(f"r: {r},c: {c}, d: {d}, t: {t}")
    # print(f"결과 - r: {r},c: {c}, d: {d}, t: {t}")
    max_ans = max(max_ans, t)

print(max_ans)