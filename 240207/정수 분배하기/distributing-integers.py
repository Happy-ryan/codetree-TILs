n, m = map(int, input().split())
nums = [int(input()) for _ in range(n)]

def get_divide(nums, q):
    cnt = 0
    for num in nums:
        cnt += num // q
    return cnt

# nums의 숫자들을 k로 나누었을 때 m개가 되게하는 k의 최댓값
def binary_search(target_m: int):
    l, r = 1, max(nums)
    # 최댓값이므로.
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if get_divide(nums, mid) >= target_m:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

print(binary_search(m))