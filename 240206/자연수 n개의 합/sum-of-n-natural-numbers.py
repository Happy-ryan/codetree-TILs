s = int(input())

def sum_val(n):
    return (n * (n + 1)) // 2


# s 보다 작은 1 ~ n까지의 합에서 n의 최댓값
# sum을 그대로 하면 시간초과가 100퍼 난다!
# 다른 방법이 필요해보인다.
def binary_search(target: int):
    l, r = 0, int(1e10)
    ans = -1
    while l <= r:
        mid = (l + r) // 2
        if sum_val(mid) <= target:
            ans = mid
            l += 1
        else:
            r -= 1

    return ans

print(binary_search(s))