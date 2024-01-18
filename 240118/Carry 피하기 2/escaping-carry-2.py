# 시간복잡도
# nC3 * n
# 완탐이 충분히 가능

from itertools import combinations

n = int(input())
numbers = [input() for _ in range(n)]


def is_carry(x, y, z):
    longest_len = max(len(x), len(y), len(z))
    carrier = [0] * longest_len
    x = '0'* (longest_len - len(x)) + x
    y = '0'* (longest_len - len(y)) + y
    z = '0'* (longest_len - len(z)) + z

    for idx in range(longest_len):
        carrier[idx] = int(x[idx]) + int(y[idx]) + int(z[idx])

    for x in carrier:
        if x > 10:
            return False
    return True


def solution():
    max_val = 0
    for x, y, z in combinations(numbers, 3):
        if is_carry(x, y, z):
            max_val = max(max_val, int(x) + int(y) + int(z))
    
    if max_val == 0:
        return -1
    return max_val

print(solution())