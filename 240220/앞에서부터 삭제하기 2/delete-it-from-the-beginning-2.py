n = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(n + 1)]
# 누적합
for i in range(n):
    prefix[i + 1] = arr[i] + prefix[i]
# 오른쪽에서부터 최솟값 기록   
# 왜 오른쪽에서부터 최솟값 기록해?
#
temp = int(1e9)
postfix = [0 for _ in range(n)]
for i in range(n - 1, -1, -1):
    postfix[i] = min(temp, arr[i])
    temp = postfix[i]

# 
total = sum(arr)
ans = 0
for k in range(1, n - 1):
    sum_val = total - prefix[k] - postfix[k]
    avg = sum_val / (n - k - 1)
    ans = max(ans, avg)

print(f"{ans:0.2f}")


# 3 1 9 2 7
# prefix [0, 3, 4, 13, 15, 22]
# postfix [1, 1, 2, 2, 7, 0]
# k = 1 || 3 / 1 9 2 7 > total - 3(1)  - 1
# k = 2 || 3 1 / 9 2 7 > total - 4(2) - 2
# k = 3 || 3 1 9 / 2 7 > total - 13(3) - 2