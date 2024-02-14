# 시간이 변수다!
# 완탐 불가능!! 
# 통과에 걸리는 시간이 너무 크다...이분탐색일 확률이 매우 높다!!

n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]
times.sort()
# 물건 모두 통과하는데 걸리는 시간 -> 이분탐색의 변수가 되겠다!
# 3초에 1개씩...3개통과 9초
# 5초에 1개씩..2개통과 10초
# 모두 통과하는데 걸리는 최소 시간 10초
# 11초 당근 통과 12초 통과!!(T)
# 9초 통과불가(F)

def get_count(final_time):
    cnt = 0
    for time in times:
        cnt +=  final_time // time
    return cnt


def binary_search(target):
    l, r = 1, 1000000000
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if get_count(mid) >= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

print(binary_search(n))