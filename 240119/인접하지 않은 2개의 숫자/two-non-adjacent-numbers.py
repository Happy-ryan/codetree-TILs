n = int(input())
nums = list(map(int, input().split()))

max_val = 0

# 시간복잡도 O(N^2)

for i in range(n):
    for j in range(n):
        # 나 자신(0), 내 양 옆(1, -1)
        if abs(i - j)>= 2:
            max_val = max(nums[i] + nums[j], max_val)

print(max_val)