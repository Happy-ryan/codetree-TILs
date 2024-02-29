# n명의 사람, m개의 수영장 라인\
# t가 1명이 한 레일을 사용하는 시간
n, m = map(int, input().split())
times = list(map(int, input().split()))
max_val = max(times)

def solution(n, m, times):
    # 적당히 자르기! 한 라인 최소 시간을 변수로...
    def get_line(max_time):
        # time - 한 라인당 최소 time보다 크게 가져가야한다!
        # time - 한 라인당 최대 max_time보다 작게 가져야한다!
        # 시간(time-X) / 레일의 수(m-Y)
        # binarysearch에서 타겟의 수 - 레일의 수다!
        cnt = 0
        standard_time = 0
        for x in times:
            if standard_time + x > max_time:
                # print("s", standard_time)
                cnt += 1
                standard_time = 0
            standard_time += x
        if standard_time > 0:
            # print("s", standard_time)
            cnt += 1
        return cnt

    def binary_search(target):
        # x - 시간, y - 레일의 수
        # 레일 1개..100,000 * 1440
        l, r = max_val, 100000 * 1440
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if get_line(mid) <= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    return binary_search(m)

print(solution(n, m, times))