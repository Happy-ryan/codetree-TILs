# 문자열을 마치 Array의 Index처럼 사용하기
n = int(input())
arr = [input() for _ in range(n)]
from collections import Counter
def solution(n, arr):
    dic = Counter(arr)
    max_val = (0, '')
    for key, value in dic.items():
        max_val = max(max_val, (value, key))

    return max_val[0]

print(solution(n, arr))