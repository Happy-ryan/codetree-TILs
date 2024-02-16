# 순차적 진행(중복선택은 절대로 안돼) & 꼭 선택할 부분
# 자기자신 + 양옆이 모두 반전!!

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, n):
    if nums[i - 1] == 0:
        cnt += 1
        nums[i - 1] = 1
        nums[i] ^= 1
        if i < n - 1:
            nums[i + 1] ^= 1

if nums[n - 1] == 0:
    print(-1)
else:
    print(cnt)