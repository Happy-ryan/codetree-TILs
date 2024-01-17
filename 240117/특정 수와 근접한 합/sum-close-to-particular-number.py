# 시간복잡도
# 제외할 숫자들: nC2
# 더하는데 sum: n
n, s = map(int, input().split())
numbers = list(map(int, input().split()))
# 방법1: 완전탐색
from itertools import combinations
total_sum = sum(numbers)
min_substract = 10001
for x, y in combinations(numbers, 2):
    sum_val = total_sum - (x + y)
    if abs(sum_val - s) < min_substract:
        min_substract = abs(sum_val - s)

print(min_substract)
# 방법2: 이분탐색