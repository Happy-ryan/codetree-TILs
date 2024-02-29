# n, m = map(int, input().split())
# points = [int(input()) for _ in range(n)]
# points.sort()
# # 두 점 사이의 최소거리를 변수로 분다!
# def get_count(dist):
#     # 가장 왼쪽은 반드시 설치
#     # 두 인접한 사이의 거리의 최솟값이 dist일 때 설치할 수 있는 곳의 수
#     # 처음 기준은 맨 왼쪽..
#     # 왼쪽1 왼쪽2 ....
#     # 왼쪽1과 왼쪽2의 차이가 최소거리보다 작아
#     # 왼쪽1 왼쪽2 왼쪽3 과 비교해여함.
#     # 기준은 왼쪽이 1이 된다.
#     # 착각: 무조건 서로 인접한 것들의 차이를 구하는 것은 아니다!
#     cnt = 1
#     standard = points[0]
#     for i in range(1, n):
#         if abs(points[i] - standard) >= dist:
#             cnt += 1
#             standard = points[i]

#     return cnt


# def binary_search(target):
#     # 거리
#     l, r = 1, max(points)
#     ans = -1
#     while l <= r:
#         mid = (l + r) // 2
#         if get_count(mid) >= target:
#             ans = mid
#             l = mid + 1
#         else:
#             r = mid -1

#     return ans

# print(binary_search(m))


# 이분탐색
n, m = map(int, input().split())
points = [int(input()) for _ in range(n)]

def solution(n, m, points):
    
    # 이분탐색의 대상이 되는 존재 - 두 물건사이의 최소거리를 변수로 둔다!
    # 최소거리를 dist라고 했을 때, 설치할 수 있는 물건의 수
    def get_material(dist):
        cnt = 1
        standard = points[0]
        for i in range(1, n):
            if abs(points[i] - standard) >= dist:
                cnt += 1
                standard = points[i]
                
        return cnt
    
    def binary_search(target):
        l, r = -1, max(points)
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if get_material(mid) >= target:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
                
        return ans
    
    return binary_search(m)

print(solution(n, m, points))