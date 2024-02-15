n, k = map(int, input().split())
points = [int(input()) for _ in range(n)]
points.sort()
inf = int(1e9)
# 좌표위치...10^9..매우 큼! -> 이분탐색
# 이분탐색의 대상: 'R'
# 폭탄의 위치는...?
# 현재 정답 기준 R이 5보다 작으면 F / 5보다 크거나 같으면 T
# (R 폭탄 R) 로 생가하지말고 2R 막대기라고 생각하자!

def get_count(r):
    max_bomb_range = -inf
    
    bomb_cnt = 0
    for point in points:
        if point > max_bomb_range:
            max_bomb_range = point + 2 * r
            bomb_cnt += 1
    return bomb_cnt

# k = 3
# 1 2   3 4 5 .. r
# 5 4 | 2 1 .. bomb_cnt(r)
# F F | T T 
# 폭탄이 최소 k개는 되야함
# k개 보다 폭탄이 적으면 나머지 폭탄은 아무데나 뿌려도 된다.
def binary_search(target):
    l, r = 0, inf
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if get_count(mid) <= target:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1

    return ans

print(binary_search(k))