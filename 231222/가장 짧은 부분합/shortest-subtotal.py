n, s = map(int, input().split())
numbers = list(map(int, input().split()))

res = 100001
sum_val =0
r = 0
for l in range(n):
    while r < n and sum_val + numbers[r] < s:
        sum_val += numbers[r]
        r += 1

    res = min(res, r - l + 1)
    sum_val -= numbers[l]

    
print(res)