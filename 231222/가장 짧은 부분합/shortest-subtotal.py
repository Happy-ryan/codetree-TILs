n, s = map(int, input().split())
numbers = [0] + list(map(int, input().split()))

# res = 100001
# sum_val = numbers[0]
# r = 0

# for l in range(n):
#     while r + 1 < n and sum_val < s:
#         sum_val += numbers[r + 1]
#         r += 1

#     if sum_val >= s:
#         res = min(res, r - l + 1)
#     sum_val -= numbers[l]

# if res == 100001:
#     print(-1)
# else:
#     print(res)

inf = 10000001
ans = inf
sum_val = 0
j = 0
for i in range(1, n + 1):
    while j + 1 <= n and sum_val < s:
        sum_val += numbers[j + 1]
        j += 1

    # 최대한 이동했는데도 sum_val이 s가 되지 못한다면..
    if sum_val < s:
        break

    # 현재 구간 [i, j]
    ans = min(ans, j - i + 1)

    # 다음 구간
    sum_val -= numbers[i]

if ans == inf:
    print(-1)
else:
    print(ans)