# 정렬은 불가
n = int(input())
nums = list(map(int, input().split()))

ans = 0
l, r = 0, 0
while r < n:
    sum_val = nums[r] - nums[l]
    if ans <= sum_val:
        ans = sum_val
    else:
        l = r
    r += 1


print(ans)