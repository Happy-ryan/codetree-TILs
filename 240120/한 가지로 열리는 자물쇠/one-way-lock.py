# 완탐: 시간복잡도 O(N^3)

n = int(input())
ans = list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        for k in range(1, n + 1):
            if abs(i - ans[0]) <= 2 or\
                abs(j - ans[1]) <= 2 or\
                abs(k - ans[2]) <= 2:
                cnt += 1

print(cnt)