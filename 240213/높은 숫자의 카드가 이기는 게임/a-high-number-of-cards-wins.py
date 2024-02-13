n = int(input())
card_b = [int(input()) for _ in range(n)]
card_b.sort()

memo = [0 for _ in range(n)]

for i in range(n):
    memo[i] = 2 * n - card_b[i] - (n - i - 1)

print(n - memo.count(0))

# n^2 이므로 완탐 불가!!
# 1 4 6
# 2 3 5 > 2, 5 > 2제출

# 1  5 - 2 = 3
# 4  2 - 1 = 1
# 6  0 = 0