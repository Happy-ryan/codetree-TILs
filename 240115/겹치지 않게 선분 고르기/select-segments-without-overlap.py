n = int(input())
cords = [list(map(int,input().split())) for _ in range(n)]

# 회의실 배정 문제와 유사해보임!
def solution(n, cords):
    cords.sort(key=lambda x: (x[1], x[0]))

    cnt = 1
    last_x = cords[0][1]
    for start_x, end_x in cords[1:]:
        # print(f"last_x: {last_x}, start_x: {start_x}, end_x: {end_x}")
        if last_x < start_x:
            last_x = end_x
            cnt += 1

    return cnt


print(solution(n, cords))