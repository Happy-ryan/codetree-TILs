# # 시간이 변수다!
# # 완탐 불가능!! 
# # 통과에 걸리는 시간이 너무 크다...이분탐색일 확률이 매우 높다!!

# n, m = map(int, input().split())
# times = [int(input()) for _ in range(m)]
# times.sort()
# # 물건 모두 통과하는데 걸리는 시간 -> 이분탐색의 변수가 되겠다!
# # 3초에 1개씩...3개통과 9초
# # 5초에 1개씩..2개통과 10초
# # 모두 통과하는데 걸리는 최소 시간 10초
# # 11초 당근 통과 12초 통과!!(T)
# # 9초 통과불가(F)

# def get_count(final_time):
#     cnt = 0
#     for time in times:
#         cnt +=  final_time // time
#     return cnt


# def binary_search(target):
#     # 각 통로가 10^9이다.
#     # n개의 물건이 통과해야하므로 최대 10^14까지...할 수 있다.
#     l, r = 1, int(1e14)
#     ans = -1
#     while l <= r:
#         mid = (l + r) // 2
#         if get_count(mid) >= target:
#             ans = mid
#             r = mid - 1
#         else:
#             l = mid + 1
#     return ans

# print(binary_search(n))
n, m = map(int, input().split())
times = [int(input()) for _ in range(m)]

def solution(n, m, times):
    # 이분탐색 - 무엇이 변수가 되냐? N개의 물건을 통과시키는데 걸리는 시간!
    # 시간(X) -> 물건의 개수(Y)로 이분탐색
    
    # 항상 이분탐색은 정렬
    times.sort()
    
    def get_time(x):
        cnt = 0
        for time in times:
            cnt += x // time
        return cnt
    
    
    def binary_search(target):
        # 시간(x),target(y)-물건의 개수
        # n개의 물건이 m개의 통로가 있을 때 시간 1e9
        # 1e5개 통로 1개(최악) 1e9 * 1e5 
        # 최소 물건 1개가 통로 1개를 지나는데 1초
        l, r = 1, int(1e14)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if get_time(mid) >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
                
        return ans
    
    return binary_search(n)

print(solution(n, m, times))