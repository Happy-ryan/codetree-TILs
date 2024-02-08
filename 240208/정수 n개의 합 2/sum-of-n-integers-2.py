n, k = map(int, input().split())
nums = list(map(int, input().split()))
psum = [0] * (n + 1)
for i in range(n):
    psum[i + 1] = nums[i] + psum[i]


ans = 0
for i in range(0, n - k + 1):
    ans = max(ans, psum[i + k] - psum[i])

print(ans)