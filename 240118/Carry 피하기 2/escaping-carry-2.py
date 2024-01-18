# 시간복잡도
# nC3 * n
# 완탐이 충분히 가능

from itertools import combinations

n = int(input())
# numbers = [input() for _ in range(n)]
number_int = [int(input()) for _ in range(n)]


def is_carry(x: str, y: str, z: str):
    longest_len = max(len(x), len(y), len(z))
    carrier = [0] * longest_len
    x = '0'* (longest_len - len(x)) + x
    y = '0'* (longest_len - len(y)) + y
    z = '0'* (longest_len - len(z)) + z

    for idx in range(longest_len):
        carrier[idx] = int(x[idx]) + int(y[idx]) + int(z[idx])

    for x in carrier:
        if x >= 10:
            return True
    return False

def is_carry_mod(x, y, z):
    # 숫자로 받아서 인덱스로 접근도 가능하다!
    # 최대 10000 
    for i in range(1, 5):
        if x % (10 ** i) // (10 ** (i - 1)) \
        + y % (10 ** i) // (10 ** (i - 1)) \
        + z % (10 ** i) // (10 ** (i - 1)) >= 10:
            return True
    # # 일의 자리
    # if x % 10 // 1 + y % 10 // 1 + z % 10 // 1 >= 10:
    #     return True
    # # 십의 자리
    # if x % 100 // 10 + y % 100 // 10 + z % 100 // 10 >= 10:
    #     return True
    # # 백의 자리
    # if x % 1000 // 100 + y % 1000 // 100 + z % 1000 // 100 >= 10:
    #     return True
    # # 천의자리
    # if x % 10000 // 1000 + y % 10000 // 1000 + z % 10000 // 1000 >= 10:
    #     return True
    return False


def solution():
    max_val = 0
    for x, y, z in combinations(numbers, 3):
        if not is_carry(x, y, z):
            max_val = max(max_val, int(x) + int(y) + int(z))
    
    if max_val == 0:
        return -1
    return max_val

def solution_():
    max_val = 0
    for x, y, z in combinations(number_int, 3):
        if not is_carry_mod(x, y, z):
            max_val = max(max_val, int(x) + int(y) + int(z))
    
    if max_val == 0:
        return -1
    return max_val

print(solution_())