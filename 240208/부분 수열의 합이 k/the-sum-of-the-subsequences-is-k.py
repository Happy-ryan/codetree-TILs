# 누적합
n, k = map(int, input().split())
nums = list(map(int, input().split()))

def solution1(n, k, nums):
    psum = [0] * (n + 1)
    for i in range(n):
        psum[i + 1] = nums[i] + psum[i]

    ans = 0
    for length in range(1, n + 1):
        for i in range(0, n - length + 1):
            if psum[i + length] - psum[i] == k:
                    ans += 1
    
    return ans


print(solution1(n, k, nums))