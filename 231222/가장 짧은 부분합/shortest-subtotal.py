n, s = map(int, input().split())
numbers = list(map(int, input().split()))

res = 100001
sum_val = numbers[0]
r = 0

for l in range(n):
    while r + 1 < n and sum_val < s:
        sum_val += numbers[r + 1]
        r += 1

    if sum_val >= s:
        res = min(res, r - l + 1)
    sum_val -= numbers[l]

if res == 100001:
    print(-1)
else:
    print(res)