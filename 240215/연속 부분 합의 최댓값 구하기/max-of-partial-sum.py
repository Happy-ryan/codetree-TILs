n = int(input())
nums = [0] + list(map(int, input().split()))
inf = int(1e9)
dp = [-inf for _ in range(n + 1)]

# dp[i]: 마지막으로 인덱스i를 '반드시' 선택했을 때, 만들 수 있는 부부분수열 합의 최대값
# '연속' 부분 수열이으모 i 입장에서는 자기만 선택하거나 바로 앞 + 자기를 선택해야한다.
# dp[i] = max(nums[i], dp[i - 1] + nums[i]) 
dp[0] = -inf
for i in range(1, n + 1):
    dp[i] = max(nums[i], dp[i - 1] + nums[i])

print(max(dp))