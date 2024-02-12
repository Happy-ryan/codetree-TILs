# 연속 부분 합의 최댓값 구하기
n = int(input())
nums = list(map(int, input().split()))
# two_pointer
def two_pointer(n, nums):
    pass


# greedy
ans = []
def greedy(n, nums):
    sum_val = 0
    s = 0
    while s < n:
        sum_val += nums[s]
        if sum_val < 0:
            sum_val = 0
        s += 1
        ans.append(sum_val)

greedy(n, nums)
print(max(ans))